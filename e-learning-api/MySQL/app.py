from flask import Flask, jsonify, request
from http import HTTPStatus
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Courses CRUD
@app.route("/api/courses", methods=["GET"])
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
def create_course():
    data = request.get_json()
    if not data or "course_name" not in data or "course_description" not in data:
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
def update_course(course_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE courses SET course_name = %s, course_description = %s WHERE course_id = %s",
            (data.get("course_name"), data.get("course_description"), course_id)
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
def create_student():
    data = request.get_json()
    if not data or "student_firstName" not in data or "student_lastName" not in data or "student_password" not in data:
        return jsonify({"success": False, "error": "student_firstName, student_lastName, and student_password are required"}), HTTPStatus.BAD_REQUEST
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
def update_student(student_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET student_firstName = %s, student_lastName = %s, student_email = %s, student_password = %s WHERE student_id = %s",
            (data.get("student_firstName"), data.get("student_lastName"), data.get("student_email"), data.get("student_password"), student_id)
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
def create_enrollment():
    data = request.get_json()
    if not data or "student_id" not in data or "course_id" not in data or "enrollment_date" not in data or "completion_date" not in data:
        return jsonify({"success": False, "error": "student_id, course_id, enrollment_date, and completion_date are required"}), HTTPStatus.BAD_REQUEST
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
def update_enrollment(enrollment_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE enrollments SET student_id = %s, course_id = %s, enrollment_date = %s, completion_date = %s WHERE enrollment_id = %s",
            (data.get("student_id"), data.get("course_id"), data.get("enrollment_date"), data.get("completion_date"), enrollment_id)
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
def create_test_result():
    data = request.get_json()
    if not data or "student_id" not in data or "test_score" not in data or "test_date" not in data:
        return jsonify({"success": False, "error": "student_id, test_score, and test_date are required"}), HTTPStatus.BAD_REQUEST
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
def update_test_result(test_result_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), HTTPStatus.BAD_REQUEST
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE test_results SET student_id = %s, test_score = %s, test_date = %s WHERE test_result_id = %s",
            (data.get("student_id"), data.get("test_score"), data.get("test_date"), test_result_id)
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