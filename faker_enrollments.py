from faker import Faker
import random
import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def populate_enrollments_table(num_records):
    fake = Faker()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT student_id FROM students")
        student_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT course_id FROM courses")
        course_ids = [row[0] for row in cursor.fetchall()]

        if not student_ids or not course_ids:
            print("No students or courses available to create enrollments.")
            return

        for _ in range(num_records):
            student_id = random.choice(student_ids)
            course_id = random.choice(course_ids)
            enrollment_date = fake.date_this_decade()
            completion_date = fake.date_between(start_date=enrollment_date, end_date="+1y")

            query = """
            INSERT INTO enrollments (student_id, course_id, enrollment_date, completion_date)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (student_id, course_id, enrollment_date, completion_date))

        conn.commit()
        print(f"{num_records} records inserted into the enrollments table.")
    except Exception as e:
        conn.rollback()
        print(f"Error populating enrollments: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("Populating enrollments table...")
    populate_enrollments_table(31)
