from pathlib import Path
from src.steam_speedster.steam.libraries import get_steam_libraries


def get_game_name(steam_path: Path | str, app_id: str) -> str:
    """Функция для получения названия игры/приложения, которое указано ближайшим в логах.

        Args:
            steam_path: Path | str
            app_id: str
        Returns:
            game_name: str
    """
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
