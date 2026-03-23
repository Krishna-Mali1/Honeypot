import sqlite3

def init_db():
    conn = sqlite3.connect("honeypot_events.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ip TEXT,
        message TEXT,
        score INTEGER
    )''')
    conn.commit()
    return conn

def log_event(db, parsed):
    c = db.cursor()
    c.execute("INSERT INTO events (timestamp, ip, message, score) VALUES (?, ?, ?, ?)", (
        parsed["timestamp"], parsed["ip"], parsed["message"], parsed["score"]
    ))
    db.commit()
    print("Event logged in SQLite")
