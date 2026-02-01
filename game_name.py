from pathlib import Path


def get_game_name(steam_path, app_id):
    steam_path = Path(steam_path)
    libraries = get_steam_libraries(steam_path)
    for library in libraries:
        app_manifest = library / "steamapps" / f"appmanifest_{app_id}.acf"
        if app_manifest.exists():
            with open(app_manifest, "r", encoding="utf-8") as f:
                for i in f:
                    if '"name"' in i:
                        return i.split('"')[3]

    return "Unknown game"


def get_steam_libraries(steam_path):
    libraries = list()
    steam_path = Path(steam_path)
    libraries.append(steam_path)
    vdf_folder_path = steam_path / "steamapps" / "libraryfolders.vdf"
    if not vdf_folder_path:
        return libraries
    with open(vdf_folder_path, mode="r", encoding="utf-8") as f:
        data = f.readlines()
        for i in data:
            line = i.strip().split('"')
            if '"path"' in i.strip():
                new_path = line[3].replace('    \\\\', '\\')
                libraries.append(Path(new_path))
    return libraries
