import re

def parse_rate(lines):
    rate = None
    for line in reversed(lines):
        if "Current download rate:" in line:
            rate = line.split()[5]
            break
    return rate

def parse_app_id(lines):
    for line in reversed(lines):
        match = re.search("AppID (\d+)", line)
        if match:
            return match.group(1)
    return None

def parse_status(lines):
    for line in reversed(lines):
        if "AppID" in line and "state changed" in line and "Queued" in line:
            return "Paused"
    return "Downloading"

