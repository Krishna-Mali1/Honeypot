# Honeypot-Based Intrusion Detection System

A real-time SSH intrusion detection system using the Cowrie Honeypot. Monitors attacker activity, scores IPs via AbuseIPDB, logs events to SQLite, 
and sends email alerts for high-risk IPs.


# How It Works

Cowrie SSH Honeypot -> Log Parser -> AbuseIPDB Reputation Check
                                          │
                              Score ≥ 50 → Email Alert
                                          │
                                    SQLite DB Log

# Project Structure

├── honeypot_logs.db
├── honeypot_events.db
├── main.py                   # Entry point
├── requirements.txt
├── config.yaml               # Configuration, add this to .gitignore
└── monitor/
    ├── honeypot_listener.py  # Tails Cowrie log in real-time
    ├── log_parser.py         # Parses login attempts and commands
    ├── reputation_checker.py # AbuseIPDB IP scoring
    ├── alert_dispatcher.py   # Email alerts via SMTP
    └── event_logger.py       # SQLite logging



# Setup

1. Install dependencies
pip install requests pyyaml


2. Configure config.yaml

log_file_path: "/opt/cowrie/var/log/cowrie/cowrie.log"

abuseipdb:
  api_key: "YOUR_API_KEY"

email:
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  sender_email: "your_email@gmail.com"
  sender_password: "your_app_password"
  recipient_email: "recipient@gmail.com"

> Note: Add config.yaml to .gitignore — it contains sensitive credentials.

3. Run
python main.py

# Requirements

- Python 3.8+
- [Cowrie SSH Honeypot](https://github.com/cowrie/cowrie) running
- [AbuseIPDB](https://www.abuseipdb.com/) API key (free tier: 1,000 checks/day)
- Gmail App Password for SMTP


# Tech Stack

| Component    | Technology          |
|--------------|---------------------|
| Honeypot     | Cowrie SSH          |
| Threat Intel | AbuseIPDB API v2    |
| Database     | SQLite3             |
| Alerts       | Gmail SMTP          |
| Language     | Python 3            |

