"""Look up customers in a SQLite database."""

import sqlite3


def find_user(db: sqlite3.Connection, user_id: int) -> tuple[str, str] | None:
    row = db.execute("SELECT name, email FROM users WHERE id = ?", (user_id,)).fetchone()
    return (row[0], row[1]) if row else None
