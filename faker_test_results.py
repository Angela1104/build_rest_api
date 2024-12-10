from faker import Faker
import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def fetch_student_ids():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT student_id FROM students")
        student_ids = [row[0] for row in cursor.fetchall()]
        return student_ids
    except Exception as e:
        print(f"Error fetching student IDs: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def populate_test_results_table(num_records, student_ids):
    fake = Faker()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        for _ in range(num_records):
            student_id = fake.random_element(elements=student_ids)
            test_score = fake.random_int(min=88, max=100) 
            test_date = fake.date_this_year()

            query = """
            INSERT INTO test_results (student_id, test_score, test_date)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (student_id, test_score, test_date))

        conn.commit()
        print(f"{num_records} records inserted into the test_results table.")
    except Exception as e:
        conn.rollback()
        print(f"Error populating test_results: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("Fetching student IDs...")
    student_ids = fetch_student_ids()
    if student_ids:
        print(f"Found {len(student_ids)} students. Populating test_results table...")
        populate_test_results_table(31, student_ids)
    else:
        print("No students found. Populate the students table first.")
