import json
import psycopg2
import os

# Database credentials
DB_NAME = "your_db"
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"

def insert_data(json_file):
    """Insert extracted data into the database."""
    if not os.path.exists(json_file):
        print(f"❌ Error: JSON file {json_file} not found!")
        return

    with open(json_file, "r") as file:
        data = json.load(file)

    if not data.get("patient_name") or not data.get("dob"):
        print("⚠️ Missing required fields in JSON! Check extracted data.")
        return

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cursor = conn.cursor()

        # Insert into Patients Table
        cursor.execute("""
            INSERT INTO patients (name, dob)
            VALUES (%s, %s) RETURNING id;
        """, (data["patient_name"], data["dob"]))
        patient_id = cursor.fetchone()[0]

        # Insert Functional Assessment
        cursor.execute("""
            INSERT INTO functional_assessment (patient_id, date, injection, exercise_therapy, difficulty_ratings, patient_changes)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (patient_id, data["date"], data["injection"] == "YES", data["exercise_therapy"] == "YES",
              json.dumps(data["difficulty_ratings"]), json.dumps(data["patient_changes"])))

        # Insert Pain Symptoms
        cursor.execute("""
            INSERT INTO pain_symptoms (patient_id, pain, tingling, burning, tightness)
            VALUES (%s, %s, %s, %s, %s);
        """, (patient_id, data["pain_symptoms"].get("Pain"), data["pain_symptoms"].get("Tingling"),
              data["pain_symptoms"].get("Burning"), data["pain_symptoms"].get("Tightness")))

        # Insert Medical Assistant Data
        cursor.execute("""
            INSERT INTO medical_assistant_data (patient_id, blood_pressure, heart_rate, weight, height, temperature, blood_glucose, respirations, spo2)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (patient_id, data["medical_assistant_data"].get("Blood Pressure"),
              data["medical_assistant_data"].get("HR"), data["medical_assistant_data"].get("Weight"),
              data["medical_assistant_data"].get("Height"), data["medical_assistant_data"].get("Temperature"),
              data["medical_assistant_data"].get("Blood Glucose"), data["medical_assistant_data"].get("Respirations"),
              data["medical_assistant_data"].get("SpO2")))

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Data inserted successfully!")

    except Exception as e:
        print(f"❌ Database insertion failed: {e}")

if __name__ == "__main__":
    insert_data("output/extracted_data.json")
