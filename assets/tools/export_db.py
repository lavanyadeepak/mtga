import sqlite3
import json
import os

db_path = r'c:\LavanyaDeepak\Projects\VoT_CitizenInitiative\assets\database\vot_ci.db'
output_path = r'c:\LavanyaDeepak\Projects\VoT_CitizenInitiative\assets\database\complaints_data.json'

def export_db_to_json():
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get complaint types
    cursor.execute("SELECT * FROM complaint_type")
    types_rows = cursor.fetchall()
    # Assuming columns are (id, name) or (id, title)
    types_columns = [description[0] for description in cursor.description]
    types_data = [dict(zip(types_columns, row)) for row in types_rows]

    # Get complaint subtypes
    cursor.execute("SELECT * FROM complaint_subtype")
    subtypes_rows = cursor.fetchall()
    subtypes_columns = [description[0] for description in cursor.description]
    subtypes_data = [dict(zip(subtypes_columns, row)) for row in subtypes_rows]

    conn.close()

    result = {
        "types": types_data,
        "subtypes": subtypes_data
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"Successfully exported data to {output_path}")

if __name__ == "__main__":
    export_db_to_json()
