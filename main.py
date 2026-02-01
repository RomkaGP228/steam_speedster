import time
from steam_path import get_windows_steam_path
from data_parser import parse_app_id, parse_rate, parse_status
from game_name import get_game_name


def read_new_lines(file_path, last_position):
    with open(file_path, "r", encoding="utf-8") as f:
        f.seek(last_position)
        lines = f.readlines()
        new_position = f.tell()

    return lines, new_position


def main():
    steam_path = get_windows_steam_path()
    content_log = f"{steam_path}/logs/content_log.txt"
    for i in range(5):
        lines, position = read_new_lines(content_log, 0)
        rate = parse_rate(lines)
        appid = parse_app_id(lines)
        status = parse_status(lines)
        if appid:
            game_name = get_game_name(steam_path, appid)
        else:
            game_name = "Unknown game"
        print(f"Minute: {i}/5 | game: {game_name} | status: {status} | rate: {rate}")
        time.sleep(60)


if __name__ == '__main__':
    main()
