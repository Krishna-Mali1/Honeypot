import yaml
from monitor.honeypot_listener import monitor_log
from monitor.log_parser import parse_log_line
from monitor.reputation_checker import check_ip
from monitor.alert_dispatcher import send_email_alert
from monitor.event_logger import init_db, log_event

print("[*] Loading config...")
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print("[*] Initializing database...")
db = init_db()

print(f"[*] Monitoring log: {config['log_file_path']}")

for line in monitor_log(config["log_file_path"]):
    print(f"[LOG] {line.strip()}")
    parsed = parse_log_line(line)
    if parsed:
        print(f"[PARSED] {parsed}")
        score = check_ip(parsed["ip"], config["abuseipdb"]["api_key"])
        parsed["score"] = score
        log_event(db, parsed)

        if score >= 50:
            print(f"ALERT: Reputation score {score}")
            send_email_alert(config, parsed)
        else:
            print(f"[!] IP reputation score {score} - no alert.")
