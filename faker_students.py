import mysql.connector
from faker import Faker
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def populate_students_table(num_records):
    fake = Faker()
    conn = get_db_connection()
    cursor = conn.cursor()

    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        query = """
        INSERT INTO students (student_firstName, student_lastName, student_email, student_password)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, email, password))

    conn.commit()
    print(f"{num_records} records inserted into the students table.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    populate_students_table(31)
