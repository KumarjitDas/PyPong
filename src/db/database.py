import os
import sqlite3
from pathlib import Path

cache_dir = Path(os.getenv('LOCALAPPDATA')) / ".cache" / "PyPong"
cache_dir.mkdir(parents=True, exist_ok=True)

DB_PATH = cache_dir / "app_data.db"
MAIN_TABLE = "game_results"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {MAIN_TABLE} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_played REAL NOT NULL,
            timestamp TEXT NOT NULL,
            p1_score INTEGER NOT NULL,
            p2_score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


__all__ = ['DB_PATH', 'MAIN_TABLE', 'get_connection', 'create_table']
