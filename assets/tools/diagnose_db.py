import sqlite3
import os

db_path = r'c:\LavanyaDeepak\Projects\VoT_CitizenInitiative\assets\database\vot_ci.db'

def diagnose_db():
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables found: {tables}")

        for table in tables:
            t_name = table[0]
            cursor.execute(f"PRAGMA table_info({t_name})")
            columns = cursor.fetchall()
            print(f"Table '{t_name}' columns: {columns}")

        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    diagnose_db()
