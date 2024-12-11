import pytest
from unittest.mock import patch, MagicMock
from app import app, create_jwt
from http import HTTPStatus

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_db_connection():
    with patch('app.get_db_connection') as mock_conn:
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        yield mock_conn

@pytest.fixture
def admin_token():
    return f"Bearer {create_jwt(user_id=1, role='admin')}"

@pytest.fixture
def student_token():
    return f"Bearer {create_jwt(user_id=2, role='student')}"

# Courses Tests
def test_create_course(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 267

    response = client.post(
        '/api/courses',
        json={
            "course_name": "Physics",
            "course_description": "A study of matter, its motion, and behavior through space and time."
        },
        headers={"Authorization": admin_token}
    )
    
    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["course_name"] == "Physics"
    assert response.json["data"]["course_id"] == 267

def test_get_courses(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        {"course_id": 262, "course_name": "Detail action behavior", "course_description": "Why change wear front director above."}
    ]

    response = client.get('/api/courses', headers={"Authorization": student_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["course_name"] == "Detail action behavior"

def test_get_course(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"course_id": 262, "course_name": "Detail action behavior", "course_description": "Why change wear front director above."}

    response = client.get('/api/courses/262', headers={"Authorization": student_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["course_name"] == "Detail action behavior"

def test_delete_course(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/courses/262', headers={"Authorization": admin_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Course with ID 262 has been deleted"

def test_update_course(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put(
        '/api/courses/262',
        json={
            "course_name": "Advanced Physics",
            "course_description": "An in-depth exploration of physics, focusing on advanced topics."
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Course updated successfully"
    
# Students Tests
def test_create_student(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 161

    response = client.post(
        '/api/students',
        json={
            "student_firstName": "Kurt Justine",
            "student_lastName": "Formiloza",
            "student_password": "kurt123",
            "student_email": "john.doe@student.com"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["student_firstName"] == "Kurt Justine"
    assert response.json["data"]["student_id"] == 161

def test_get_students(client, mock_db_connection, admin_token): 
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        {"student_id": 131, "student_firstName": "Regina", "student_lastName": "Jackson"}
    ]
    
    response = client.get('/api/students', headers={"Authorization": admin_token})
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["student_firstName"] == "Regina"
    assert response.json["success"] is True
    assert "data" in response.json
    assert "total" in response.json

def test_get_student(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"student_id": 131, "student_firstName": "Regina", "student_lastName": "Jackson"}

    response = client.get('/api/students/131', headers={"Authorization": student_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["student_firstName"] == "Regina"

def test_update_student(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put(
        '/api/students/131',
        json={
            "student_firstName": "Regine",
            "student_lastName": "Jackson",
            "student_password": "newpassword",
            "student_email": "regine.jackson@student.com"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Student updated successfully"

def test_delete_student(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/students/131', headers={"Authorization": admin_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Student with ID 131 has been deleted"

# Enrollments Tests
def test_create_enrollment(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 301

    response = client.post(
        '/api/enrollments',
        json={
            "student_id": 131,
            "course_id": 262,
            "enrollment_date": "2023-12-01",
            "completion_date": "2024-12-01"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["enrollment_id"] == 301

def test_get_enrollments(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        {"enrollment_id": 301, "student_id": 131, "course_id": 262}
    ]

    response = client.get('/api/enrollments', headers={"Authorization": student_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["student_id"] == 131
    
def test_get_enrollment(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"enrollment_id": 301, "student_id": 131, "course_id": 262}

    response = client.get('/api/enrollments/301', headers={"Authorization": student_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["student_id"] == 131

def test_update_enrollment(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put(
        '/api/enrollments/301',
        json={
            "student_id": 131,
            "course_id": 262,
            "enrollment_date": "2023-12-05",
            "completion_date": "2025-12-05"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Enrollment updated successfully"

def test_delete_enrollment(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/enrollments/301', headers={"Authorization": admin_token})
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Enrollment with ID 301 has been deleted"
    
# Test Results Tests
def test_create_test_result(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 123

    response = client.post(
        '/api/test_results',
        json={
            "student_id": 1,
            "test_score": 95,
            "test_date": "2024-12-01"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["test_score"] == 95
    assert response.json["data"]["test_result_id"] == 123

def test_get_test_results(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        {"test_result_id": 123, "student_id": 1, "test_score": 95, "test_date": "2024-12-01"}
    ]

    response = client.get('/api/test_results', headers={"Authorization": student_token})

    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["test_score"] == 95

def test_get_test_result(client, mock_db_connection, student_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {
        "test_result_id": 123, "student_id": 1, "test_score": 95, "test_date": "2024-12-01"
    }

    response = client.get('/api/test_results/123', headers={"Authorization": student_token})

    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["test_score"] == 95

def test_update_test_result(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put(
        '/api/test_results/123',
        json={
            "student_id": 1,
            "test_score": 98,
            "test_date": "2024-12-05"
        },
        headers={"Authorization": admin_token}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Test result updated successfully"

def test_delete_test_result(client, mock_db_connection, admin_token):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/test_results/123', headers={"Authorization": admin_token})

    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Test result with ID 123 has been deleted"