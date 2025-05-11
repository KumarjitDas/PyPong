from src.db import get_connection, MAIN_TABLE


def insert_entry(value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {MAIN_TABLE} (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()


def get_all_entries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {MAIN_TABLE}")
    rows = cursor.fetchall()
    conn.close()
    return rows


__all__ = ['insert_entry', 'get_all_entries']
