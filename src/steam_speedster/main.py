import time
from src.steam_speedster.steam.steam_path import get_windows_steam_path
from src.steam_speedster.logs.data_parser import parse_app_id, parse_rate, parse_status
from src.steam_speedster.steam.name_reader import get_game_name
from pathlib import Path


def read_new_lines(file_path, last_position):
    with open(file_path, "r", encoding="utf-8") as f:
        f.seek(last_position)
        lines = f.readlines()
        new_position = f.tell()

    return lines, new_position


def main():
    try:
        steam_path = get_windows_steam_path()
        content_log = Path(steam_path) / "logs" / "content_log.txt"
        for i in range(5):
            lines, position = read_new_lines(content_log, 0)
            rate = parse_rate(lines)
            app_id = parse_app_id(lines)
            status = parse_status(lines)
            if app_id:
                game_name = get_game_name(steam_path, app_id)
            else:
                game_name = "Unknown game"
            print(f"Minute: {i + 1}/5 | game: {game_name} | status: {status} | rate: {rate}")
            time.sleep(60)
    except KeyboardInterrupt:
        print("Monitoring stopped by user")


if __name__ == '__main__':
    main()
