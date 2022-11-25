from ctypes import WinDLL, c_int
from ctypes.wintypes import MSG
from threading import Thread, Event
from typing import Callable

from win32api import GetAsyncKeyState, mouse_event, OpenProcess, CloseHandle, EnumDisplaySettings, SetConsoleCtrlHandler
from win32con import WH_MOUSE_LL, WM_MOUSEWHEEL, WM_QUIT, MOUSEEVENTF_HWHEEL, MOUSEEVENTF_WHEEL, MAXIMUM_ALLOWED
from win32gui import GetCursorPos, WindowFromPoint
from win32process import GetWindowThreadProcessId, GetModuleFileNameEx

from smoothscroll.models import SmoothScrollConfig, LowLevelMouseProc

user32 = WinDLL('user32', use_last_error=True)


class MouseListener(Thread):
    def __init__(self, callback: Callable, config: SmoothScrollConfig, *args: object, **kwargs: object):
        super().__init__(*args, **kwargs)
        self._callback = callback
        self.config = config

        self._stop_event = Event()

    def run(self):
        mouse_callback = LowLevelMouseProc(self._low_level_mouse_handler)
        mouse_hook = user32.SetWindowsHookExA(
            WH_MOUSE_LL,
            mouse_callback,
            c_int(0),
            c_int(0)
        )

        msg = MSG()
        while bRet := user32.GetMessageW(msg, c_int(0), c_int(0), c_int(0)):
            if bRet == -1:
                break
            user32.TranslateMessage(msg)
            user32.DispatchMessageA(msg)

        user32.UnhookWindowsHookEx(mouse_hook)

        self._stop_event.set()

    def _low_level_mouse_handler(self, n_code, w_param, l_param):
        if w_param == WM_MOUSEWHEEL:
            if not l_param.contents.reserved:
                scroll_config = None
                current_app_path = get_current_app_path()
                for app_config in self.config.app_configs:
                    if current_app_path == app_config.path or app_config.regexp.match(current_app_path):
                        scroll_config = app_config.scroll_config
                if scroll_config:
                    self._callback(
                        l_param.contents.data / (2 << 15) * (-1 if scroll_config.inverted else 1),
                        bool(GetAsyncKeyState(scroll_config.horizontal_scroll_key)),
                        scroll_config
                    )
                    return 1  # to prevent processing by the system
        return user32.CallNextHookEx(c_int(0), n_code, w_param, l_param)

    def listen(self) -> None:
        self._stop_event.wait()

    def quit(self) -> None:
        user32.PostThreadMessageW(self.native_id, WM_QUIT, c_int(0), c_int(0))

    def join(self, timeout=None):
        self.quit()
        super().join(timeout=timeout)


def scroll(delta: int, is_horizontal: bool = False) -> None:
    mouse_event(MOUSEEVENTF_HWHEEL if is_horizontal else MOUSEEVENTF_WHEEL, 0, 0, delta, 0)


def get_current_app_path() -> str:
    cursor_pos = GetCursorPos()
    active_hwnd = WindowFromPoint(cursor_pos)
    tid, pid = GetWindowThreadProcessId(active_hwnd)
    h_process = OpenProcess(MAXIMUM_ALLOWED, 0, pid)
    current_app_path = GetModuleFileNameEx(h_process, None)
    CloseHandle(h_process)
    return current_app_path.replace('\\', r'/')


def get_display_frequency() -> int:
    return EnumDisplaySettings(None, -1).DisplayFrequency


def set_console_ctrl_handler(callback: Callable) -> None:
    SetConsoleCtrlHandler(callback, True)
