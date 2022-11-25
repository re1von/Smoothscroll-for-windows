import easing_functions
from win32con import VK_SHIFT

from smoothscroll import (SmoothScroll,
                          SmoothScrollConfig, AppConfig, ScrollConfig)

if __name__ == '__main__':
    SmoothScroll(
        config=SmoothScrollConfig(
            app_config=[
                AppConfig(
                    regexp=r'.*',
                    scroll_config=ScrollConfig(
                        distance=None,  # [px] None - automatic detection by the system (default=120)
                        acceleration=1.,  # [x] scroll down acceleration
                        opposite_acceleration=1.2,  # [x] scroll up acceleration
                        acceleration_delta=70,  # [ms]
                        acceleration_max=14,  # [x] max acceleration steps
                        duration=200,  # [ms]
                        pulse_scale=3,  # [x] tail to head ratio
                        ease=easing_functions.LinearInOut,  # Easing function
                        inverted=False,  # down, up = up, down
                        horizontal_scroll_key=VK_SHIFT  # VK_SHIFT, VK_CONTROL, VK_MENU
                    ),
                ),
                AppConfig(
                    path='C:/Windows/explorer.exe',
                    enabled=False
                ),
                AppConfig(
                    path='C:/Program Files/Genshin Impact/Genshin Impact game/GenshinImpact.exe',
                    enabled=False
                ),
                AppConfig(
                    regexp=r'.*pycharm64\.exe.*',
                    enabled=False
                ),
                AppConfig(
                    path='C:/Program Files/Adobe/Adobe Illustrator 2023/Support Files/Contents/Windows/Illustrator.exe',
                    enabled=False
                ),
            ]
        )
    ).start(is_block=True)
