import re
from datetime import datetime

def parse_log_line(line):
    match_cmd = re.search(r'\[(HoneyPotSSHTransport|SSHTransport),\d+,([\d\.]+)\]\s+CMD: (.+)', line)
    if match_cmd:
        _, ip, cmd = match_cmd.groups()
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "ip": ip,
            "message": f"Command issued: {cmd}"
        }

    match_login = re.search(r'\[(HoneyPotSSHTransport|SSHTransport),\d+,([\d\.]+)\]\s+login attempt \[b\'(.+?)\'/b\'(.+?)\'\] (succeeded|failed)', line)
    if match_login:
        _, ip, username, password, status = match_login.groups()
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "ip": ip,
            "message": f"Login {status} with username '{username}' and password '{password}'"
        }

    return None
