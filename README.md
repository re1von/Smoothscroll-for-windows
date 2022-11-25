# Smoothscroll-for-windows
![python version required](https://img.shields.io/static/v1?label=python&message=v3.11&color=0374b4&link=https://github.com/re1von/Smoothscroll-for-windows)  
A free & simple script in python allow your mouse wheel to scroll smoothly on Windows 10/11.  
![preview](https://github.com/re1von/Smoothscroll-for-windows/blob/main/project-assets/preview.gif)

## Features
- Let the mouse wheel scroll smoothly in all apps.
- Allows customizing scroll behavior, such as the speed and acceleration.
- Individual configuration for each app with the possibility of disabling it.

## Requirements
- python >= 3.11
- requirements.txt  
  - `python -m pip install -r requirements.txt`

## Usage example
`python main.py`

## Build example
`pyinstaller --onefile --name SmoothScroll.exe --noconsole main.py`  
*Please don't use pyinstaller, wait for [nuitka](https://github.com/Nuitka/Nuitka) to add support for python3.11

## Dev tools
- app-picker.py - outputs the absolute path to the executable file (.exe) under the cursor every second.

## Thanks
- [Smoothscroll-for-websites](https://github.com/galambalazs/smoothscroll-for-websites)
