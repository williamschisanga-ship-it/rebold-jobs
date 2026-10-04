import sqlite3

DB_PATH = "rebold.db"


def get_connection():
    """Open a connection to the database file (it is created if it doesn't exist)."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables(conn):
    """Create the tables if they don't already exist."""
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS clients (
        client_id   INTEGER PRIMARY KEY,
        full_name   TEXT NOT NULL,
        phone       TEXT NOT NULL UNIQUE,
        location    TEXT,
        source      TEXT,
        created_at  TEXT DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS services (
        service_id  INTEGER PRIMARY KEY,
        name        TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS jobs (
        job_id           INTEGER PRIMARY KEY,
        client_id        INTEGER NOT NULL REFERENCES clients(client_id),
        job_type         TEXT NOT NULL CHECK (job_type IN ('service', 'supply')),
        service_id       INTEGER REFERENCES services(service_id),
        status           TEXT NOT NULL DEFAULT 'request_received',
        next_action      TEXT,
        next_action_due  TEXT,
        created_at       TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)


SERVICES = [
    "Camera installation",
    "Gate motor installation",
    "Repairs and maintenance",
    "Paving",
    "Building",
    "Painting",
]


def seed_services(conn):
    """Fill the services table with Rebold's services."""
    conn.executemany(
        "INSERT OR IGNORE INTO services (name) VALUES (?)",
        [(name,) for name in SERVICES],
    )
    conn.commit()


if __name__ == "__main__":
    conn = get_connection()
    create_tables(conn)
    seed_services(conn)

    print("Services in the database:")
    for row in conn.execute("SELECT service_id, name FROM services"):
        print(row)

    conn.close()
    git add database.py
    git commit -m "Create database with clients, services and jobs tables"
    git push

    
