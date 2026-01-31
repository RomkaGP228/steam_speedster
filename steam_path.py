import winreg

def get_windows_steam_path():
    try:
        main_path = r"Software\Valve\Steam"
        hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, main_path)
        path, code = winreg.QueryValueEx(hkey, "SteamPath")
        hkey.Close()
        return path
    except FileNotFoundError:
        print("Steam not found.")
        return None
    except Exception as e:
        print(f"An error while reading: {e}")
        return None

steam_location = get_windows_steam_path()
if steam_location:
    print(f"Steam установлен в: {steam_location}")
