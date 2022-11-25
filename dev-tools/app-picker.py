from time import sleep

import win32api
import win32con
import win32gui
import win32process

previous_app_path = None


def get_current_app_path() -> str:
    cursor_pos = win32gui.GetCursorPos()
    current_hwnd = win32gui.WindowFromPoint(cursor_pos)
    tid, pid = win32process.GetWindowThreadProcessId(current_hwnd)
    current_process = win32api.OpenProcess(win32con.MAXIMUM_ALLOWED, 0, pid)
    current_app_path = win32process.GetModuleFileNameEx(current_process, None)
    win32api.CloseHandle(current_process)
    return current_app_path


if __name__ == '__main__':
    try:
        while app_path := get_current_app_path():
            if app_path != previous_app_path:
                print(previous_app_path := app_path.replace('\\', r'/'))
            sleep(1)
    except KeyboardInterrupt:
        pass
