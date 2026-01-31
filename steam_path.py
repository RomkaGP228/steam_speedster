# import winreg
#
#
# def get_windows_steam_path():
#     try:
#         main_path = r"Software\Valve\Steam"
#         hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, main_path)
#         path, code = winreg.QueryValueEx(hkey, "SteamPath")
#         hkey.Close()
#         return path
#     except FileNotFoundError:
#         print("Steam not found.")
#         return None
#     except Exception as e:
#         print(f"An error while reading: {e}")
#         return None
#
#
#
#
# steam_location = get_windows_steam_path()
# if steam_location:
#     print(f"Steam установлен в: {steam_location}")

import os
from pathlib import Path


def get_linux_steam_path():
    # Получаем путь к домашней директории пользователя
    home = Path.home()

    # Список возможных путей установки
    possible_paths = [
        home / ".local/share/Steam",
        home / ".steam/steam",
        home / ".var/app/com.valvesoftware.Steam/.local/share/Steam",  # Flatpak
        home / "snap/steam/common/.local/share/Steam"  # Snap
    ]

    for path in possible_paths:
        # Проверяем, существует ли директория и есть ли в ней папка steamapps
        if path.exists() and (path / "steamapps").exists():
            return str(path)

    return None


# Проверка
path = get_linux_steam_path()
if path:
    print(f"Steam найден по пути: {path}")
else:
    print("Steam не найден.")