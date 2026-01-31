def get_game_name(steam_path, app_id):
    app_manifest = steam_path / "steamapps" / f"appmanifest_{app_id}.acf"
    if not app_manifest:
        return "Unknown game"
    with open(app_manifest, "r", encoding="utf-8") as f:
        for i in f:
            if '"name"' in i:
                return i.split('"')[3]

    return "Unknown game"

