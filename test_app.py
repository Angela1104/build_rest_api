import pytest
from unittest.mock import patch, MagicMock
from app import app
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

# Courses Tests
def test_create_course(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 267

    response = client.post('/api/courses', json={
        "course_name": "Physics",
        "course_description": "A study of matter, its motion, and behavior through space and time."
    })
    
    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["course_name"] == "Physics"
    assert response.json["data"]["course_id"] == 267

def test_get_courses(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        {"course_id": 262, "course_name": "Detail action behavior", "course_description": "Why change wear front director above."}
    ]

    response = client.get('/api/courses')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["course_name"] == "Detail action behavior"

def test_get_course(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"course_id": 262, "course_name": "Detail action behavior", "course_description": "Why change wear front director above."}

    response = client.get('/api/courses/262')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["course_name"] == "Detail action behavior"

def test_update_course(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put('/api/courses/262', json={
        "course_name": "Updated Physics",
        "course_description": "Updated description of physics."
    })
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["course_name"] == "Updated Physics"

def test_delete_course(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/courses/262')
    
    assert response.status_code == HTTPStatus.NO_CONTENT

# Enrollments CRUD Tests
def test_create_enrollment(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 201

    response = client.post('/api/enrollments', json={
        "student_id": 131,
        "course_id": 262,
        "enrollment_date": "2023-12-10",
        "completion_date": "2025-12-10"
    })
    
    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["enrollment_id"] == 201

def test_get_enrollments(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [{"enrollment_id": 151, "student_id": 137, "course_id": 266}]

    response = client.get('/api/enrollments')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["student_id"] == 137

def test_get_enrollment(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"enrollment_id": 151, "student_id": 137, "course_id": 266}

    response = client.get('/api/enrollments/151')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["student_id"] == 137

def test_update_enrollment(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put('/api/enrollments/151', json={
        "student_id": 137,
        "course_id": 262,
        "enrollment_date": "2023-12-10",
        "completion_date": "2025-12-10"
    })
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["course_id"] == 262

# Students Tests
def test_create_student(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 161

    response = client.post('/api/students', json={
        "student_firstName": "John",
        "student_lastName": "Doe",
        "student_password": "password123",
        "student_email": "john.doe@example.com"
    })

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["student_firstName"] == "John"
    assert response.json["data"]["student_id"] == 161

def test_get_students(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [{"student_id": 131, "student_firstName": "Regina", "student_lastName": "Jackson"}]

    response = client.get('/api/students')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["student_firstName"] == "Regina"

def test_get_student(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"student_id": 131, "student_firstName": "Regina", "student_lastName": "Jackson"}

    response = client.get('/api/students/131')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["student_firstName"] == "Regina"

def test_update_student(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1
    
    response = client.put('/api/students/131', json={
        "student_firstName": "Regine",
        "student_lastName": "Jackson",
        "student_password": "@cftg&/hyg",
        "student_email": "regine@example.com"
    })
    
    print(response.json)
    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Student updated successfully"

def test_update_student_missing_required_fields(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 0
    
    response = client.put('/api/students/131', json={
        "student_firstName": "Regine"
    })
    
    print(response.json)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json["error"] == "student_firstName and student_lastName are required"

def test_delete_student(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.delete('/api/students/135')
    
    assert response.status_code == HTTPStatus.NO_CONTENT

# Test Results Tests
def test_create_test_result(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.lastrowid = 474

    response = client.post('/api/test_results', json={
        "student_id": 131,
        "test_score": 92.00,
        "test_date": "2024-12-10"
    })

    assert response.status_code == HTTPStatus.CREATED
    assert response.json["data"]["test_result_id"] == 474

def test_get_test_results(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [{"test_result_id": 444, "student_id": 155, "test_score": 91.00}]

    response = client.get('/api/test_results')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["total"] == 1
    assert response.json["data"][0]["test_score"] == 91.00

def test_get_test_result(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.fetchone.return_value = {"test_result_id": 444, "student_id": 155, "test_score": 91.00}

    response = client.get('/api/test_results/444')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json["data"]["test_score"] == 91.00

def test_update_test_result(client, mock_db_connection):
    mock_cursor = mock_db_connection.return_value.cursor.return_value
    mock_cursor.rowcount = 1

    response = client.put('/api/test_results/444', json={
        "student_id": 155,
        "test_score": 98.00,
        "test_date": "2024-07-10"
    })
    print(response.json)
    assert response.status_code == HTTPStatus.OK
    assert response.json["success"] is True
    assert response.json["message"] == "Test result updated successfully"

