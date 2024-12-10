from faker import Faker
import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def populate_courses_table(num_records):
    fake = Faker()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        for _ in range(num_records):
            course_name = fake.sentence(nb_words=3) 
            course_description = fake.paragraph(nb_sentences=5) 

            query = """
            INSERT INTO courses (course_name, course_description)
            VALUES (%s, %s)
            """
            cursor.execute(query, (course_name, course_description))

        conn.commit()
        print(f"{num_records} records inserted into the courses table.")
    except Exception as e:
        conn.rollback()
        print(f"Error populating courses: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("Populating courses table...")
    populate_courses_table(5)  
