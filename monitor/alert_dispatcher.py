import smtplib
from email.message import EmailMessage

def send_email_alert(config, parsed):
    try:
        msg = EmailMessage()
        msg["Subject"] = f" Honeypot Alert: {parsed['ip']}"
        msg["From"] = config["email"]["sender_email"]
        msg["To"] = config["email"]["recipient_email"]
        msg.set_content(f"""
 Honeypot Alert 

IP Address: {parsed['ip']}
Reputation Score: {parsed['score']}
Event: {parsed['message']}
Timestamp: {parsed['timestamp']}
        """)

        with smtplib.SMTP(config["email"]["smtp_server"], config["email"]["smtp_port"]) as server:
            server.starttls()
            server.login(config["email"]["sender_email"], config["email"]["sender_password"])
            server.send_message(msg)
        print(f"Email alert sent to {config['email']['recipient_email']}")
    except Exception as e:
        print(f"[!] Email alert failed: {e}")
