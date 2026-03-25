import sqlite3
import json
import os

db_path = r'c:\LavanyaDeepak\Projects\VoT_CitizenInitiative\assets\database\vot_ci.db'
output_path = r'c:\LavanyaDeepak\Projects\VoT_CitizenInitiative\assets\database\complaints_data.json'

def export_db_to_json():
    print(f"Opening database at {db_path}...")
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get complaint types
        print("Fetching complaint types...")
        cursor.execute("SELECT * FROM complaint_type")
        types_rows = cursor.fetchall()
        types_columns = [description[0] for description in cursor.description]
        types_data = [dict(zip(types_columns, row)) for row in types_rows]

        # Get complaint subtypes
        print("Fetching complaint subtypes...")
        cursor.execute("SELECT * FROM complaint_subtype")
        subtypes_rows = cursor.fetchall()
        subtypes_columns = [description[0] for description in cursor.description]
        subtypes_data = [dict(zip(subtypes_columns, row)) for row in subtypes_rows]

        conn.close()

        result = {
            "types": types_data,
            "subtypes": subtypes_data
        }

        print(f"Writing {len(types_data)} types and {len(subtypes_data)} subtypes to {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print("Successfully exported data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    export_db_to_json()
