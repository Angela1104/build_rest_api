import re
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from http import HTTPStatus
import mysql.connector
from config import DB_CONFIG
import jwt
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

SECRET_KEY = "angela"

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()  
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.InvalidTokenError:
        return None  

# Register route
@app.route("/api/register", methods=["POST"])
def register_user():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"success": False, "error": "Email and password are required"}), HTTPStatus.BAD_REQUEST

    email = data["email"]
    password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
        return jsonify({"success": True, "message": "User registered successfully"}), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

# Login route
@app.route("/api/login", methods=["POST"])
def login_user():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"success": False, "error": "Email and password are required"}), HTTPStatus.BAD_REQUEST

    email = data["email"]
    password = data["password"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user["password"], password):
            token = create_jwt(user["id"])
            return jsonify({"success": True, "token": token}), HTTPStatus.OK
        else:
            return jsonify({"success": False, "error": "Invalid email or password"}), HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

def token_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"success": False, "error": "Token is missing"}), HTTPStatus.UNAUTHORIZED

        token = token.split(" ")[1] 
        payload = verify_jwt(token)
        if not payload:
            return jsonify({"success": False, "error": "Token is invalid or expired"}), HTTPStatus.UNAUTHORIZED

        request.user = payload
        return f(*args, **kwargs)

    return decorated

# Courses CRUD
@app.route("/api/courses", methods=["GET"])
@token_required
def get_courses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        return jsonify({"success": True, "data": courses, "total": len(courses)}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/courses/<int:course_id>", methods=["GET"])
@token_required
def get_course(course_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses WHERE course_id = %s", (course_id,))
        course = cursor.fetchone()
        if not course:
            return jsonify({"success": False, "error": "Course not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "data": course}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/courses", methods=["POST"])
@token_required
def create_course():
    data = request.get_json()
    if not data or not data.get("course_name") or not data.get("course_description"):
        return jsonify({"success": False, "error": "course_name and course_description are required"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (course_name, course_description) VALUES (%s, %s)",
            (data["course_name"], data["course_description"])
        )
        conn.commit()
        new_course_id = cursor.lastrowid
        return jsonify({"success": True, "data": {"course_id": new_course_id, "course_name": data["course_name"], "course_description": data["course_description"]}}), HTTPStatus.CREATED
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/courses/<int:course_id>", methods=["PUT"])
@token_required
def update_course(course_id):
    data = request.get_json()
    
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST
    
    if not data.get("course_name") or not data.get("course_description"):
        return jsonify({"success": False, "error": "course_name and course_description are required"}), HTTPStatus.BAD_REQUEST

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE courses SET course_name = %s, course_description = %s WHERE course_id = %s",
            (data["course_name"], data["course_description"], course_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Course not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": "Course updated successfully"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
@token_required
def delete_course(course_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Course not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": f"Course with ID {course_id} has been deleted"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

# Students CRUD
@app.route("/api/students", methods=["GET"])
@token_required
def get_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return jsonify({"success": True, "data": students, "total": len(students)}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/students/<int:student_id>", methods=["GET"])
@token_required
def get_student(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        student = cursor.fetchone()
        if not student:
            return jsonify({"success": False, "error": "Student not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "data": student}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/students", methods=["POST"])
@token_required
def create_student():
    data = request.get_json()
    if not data or not data.get("student_firstName") or not data.get("student_lastName") or not data.get("student_password"):
        return jsonify({"success": False, "error": "student_firstName, student_lastName, and student_password are required"}), HTTPStatus.BAD_REQUEST
    if data.get("student_email") and not is_valid_email(data["student_email"]):
        return jsonify({"success": False, "error": "Invalid email format"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (student_firstName, student_lastName, student_email, student_password) VALUES (%s, %s, %s, %s)",
            (data["student_firstName"], data["student_lastName"], data.get("student_email"), data["student_password"])
        )
        conn.commit()
        new_student_id = cursor.lastrowid
        return jsonify({"success": True, "data": {"student_id": new_student_id, **data}}), HTTPStatus.CREATED
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/students/<int:student_id>", methods=["PUT"])
@token_required
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST

    if not data.get("student_firstName") or not data.get("student_lastName"):
        return jsonify({"success": False, "error": "student_firstName and student_lastName are required"}), HTTPStatus.BAD_REQUEST

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET student_firstName = %s, student_lastName = %s, student_email = %s, student_password = %s WHERE student_id = %s",
            (data["student_firstName"], data["student_lastName"], data.get("student_email"), data.get("student_password"), student_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Student not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": "Student updated successfully"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/students/<int:student_id>", methods=["DELETE"])
@token_required
def delete_student(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Student not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": f"Student with ID {student_id} has been deleted"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

# Enrollments CRUD
@app.route("/api/enrollments", methods=["GET"])
@token_required
def get_enrollments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM enrollments")
        enrollments = cursor.fetchall()
        return jsonify({"success": True, "data": enrollments, "total": len(enrollments)}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/enrollments/<int:enrollment_id>", methods=["GET"])
@token_required
def get_enrollment(enrollment_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM enrollments WHERE enrollment_id = %s", (enrollment_id,))
        enrollment = cursor.fetchone()
        if not enrollment:
            return jsonify({"success": False, "error": "Enrollment not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "data": enrollment}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/enrollments", methods=["POST"])
@token_required
def create_enrollment():
    data = request.get_json()
    if not data or not data.get("student_id") or not data.get("course_id") or not data.get("enrollment_date") or not data.get("completion_date"):
        return jsonify({"success": False, "error": "student_id, course_id, enrollment_date, and completion_date are required"}), HTTPStatus.BAD_REQUEST
    if not is_valid_date(data["enrollment_date"]) or not is_valid_date(data["completion_date"]):
        return jsonify({"success": False, "error": "Invalid date format. Expected YYYY-MM-DD"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id, enrollment_date, completion_date) VALUES (%s, %s, %s, %s)",
            (data["student_id"], data["course_id"], data["enrollment_date"], data["completion_date"])
        )
        conn.commit()
        new_enrollment_id = cursor.lastrowid
        return jsonify({"success": True, "data": {"enrollment_id": new_enrollment_id, **data}}), HTTPStatus.CREATED
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/enrollments/<int:enrollment_id>", methods=["PUT"])
@token_required
def update_enrollment(enrollment_id):
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST

    if not data.get("student_id") or not data.get("course_id") or not data.get("enrollment_date") or not data.get("completion_date"):
        return jsonify({"success": False, "error": "student_id, course_id, enrollment_date, and completion_date are required"}), HTTPStatus.BAD_REQUEST

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE enrollments SET student_id = %s, course_id = %s, enrollment_date = %s, completion_date = %s WHERE enrollment_id = %s",
            (data["student_id"], data["course_id"], data["enrollment_date"], data["completion_date"], enrollment_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Enrollment not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": "Enrollment updated successfully"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/enrollments/<int:enrollment_id>", methods=["DELETE"])
@token_required
def delete_enrollment(enrollment_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM enrollments WHERE enrollment_id = %s", (enrollment_id,))
        result = cursor.fetchone()
               
        if result is None:
            return jsonify({"success": False, "error": "Enrollment not found"}), HTTPStatus.NOT_FOUND

        return jsonify({"success": False, "error": "Deletion not allowed due to foreign key constraints"}), HTTPStatus.FORBIDDEN

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

    finally:
        cursor.close()
        conn.close()
        
# Test Results CRUD
@app.route("/api/test_results", methods=["GET"])
@token_required
def get_test_results():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM test_results")
        test_results = cursor.fetchall()
        return jsonify({"success": True, "data": test_results, "total": len(test_results)}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/test_results/<int:test_result_id>", methods=["GET"])
@token_required
def get_test_result(test_result_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM test_results WHERE test_result_id = %s", (test_result_id,))
        test_result = cursor.fetchone()
        if not test_result:
            return jsonify({"success": False, "error": "Test result not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "data": test_result}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/test_results", methods=["POST"])
@token_required
def create_test_result():
    data = request.get_json()
    if not data or not data.get("student_id") or not data.get("test_score") or not data.get("test_date"):
        return jsonify({"success": False, "error": "student_id, test_score, and test_date are required"}), HTTPStatus.BAD_REQUEST
    if not isinstance(data["test_score"], (int, float)) or not (0 <= data["test_score"] <= 100):
        return jsonify({"success": False, "error": "test_score must be a number between 0 and 100"}), HTTPStatus.BAD_REQUEST
    if not is_valid_date(data["test_date"]):
        return jsonify({"success": False, "error": "Invalid date format for test_date. Expected YYYY-MM-DD"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test_results (student_id, test_score, test_date) VALUES (%s, %s, %s)",
            (data["student_id"], data["test_score"], data["test_date"])
        )
        conn.commit()
        new_test_result_id = cursor.lastrowid
        return jsonify({"success": True, "data": {"test_result_id": new_test_result_id, **data}}), HTTPStatus.CREATED
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/test_results/<int:test_result_id>", methods=["PUT"])
@token_required
def update_test_result(test_result_id):
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST

    if not data.get("student_id") or not data.get("test_score") or not data.get("test_date"):
        return jsonify({"success": False, "error": "student_id, test_score, and test_date are required"}), HTTPStatus.BAD_REQUEST

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE test_results SET student_id = %s, test_score = %s, test_date = %s WHERE test_result_id = %s",
            (data["student_id"], data["test_score"], data["test_date"], test_result_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"success": False, "error": "Test result not found"}), HTTPStatus.NOT_FOUND
        return jsonify({"success": True, "message": "Test result updated successfully"}), HTTPStatus.OK
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        cursor.close()
        conn.close()

@app.route("/api/test_results/<int:test_result_id>", methods=["DELETE"])
@token_required
def delete_test_result(test_result_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_results WHERE test_result_id = %s", (test_result_id,))
        result = cursor.fetchone()
        
        if result is None:
            return jsonify({"success": False, "error": "Test result not found"}), HTTPStatus.NOT_FOUND

        return jsonify({"success": False, "error": "Deletion not allowed due to foreign key constraints"}), HTTPStatus.FORBIDDEN

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)