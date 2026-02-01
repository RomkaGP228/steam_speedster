import re


def parse_rate(lines: list[str]):
    """Функция для парсинга нынешней скорости загрузки из файла content_log
        Args:
            lines: list[str]
        Returns:
            str
    """
    rate = None
    for line in reversed(lines):
        if "Current download rate:" in line:
            rate = line.split()[5]
            break
    return rate


def parse_app_id(lines: list[str]):
    """Функция для парсинга id приложения, ближайшего в логах
        Args:
            lines: list[str]
        Returns:
            str
    """
    for line in reversed(lines):
        match = re.search(r"\bAppID\s+(\d+)\b", line)
        if match:
            return match.group(1)
    return None


def parse_status(lines: list[str]):
    """Функция для парсинга статуса последнего приложения
            Args:
                lines: list[str]
            Returns:
                str
        """
    for line in reversed(lines):
        if ("AppID" in line) and ("changed" in line) and ("Suspended" in line):
            return "Paused"
        elif ("AppID" in line) and ("changed" in line) and ("Downloading" in line):
            return "Downloading"
        elif ("AppID" in line) and ("changed" in line) and ("Fully Installed" in line):
            return "Downloaded"
    return "Downloading"
