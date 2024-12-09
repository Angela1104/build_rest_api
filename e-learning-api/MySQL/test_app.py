import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Courses Tests
def test_get_courses(client):
    response = client.get("/api/courses")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_get_course(client):
    response = client.get("/api/courses/200")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_create_course(client):
    new_course = {
        "course_name": "Programming Language",
        "course_description": "structure of compilers and interpreters."
    }
    response = client.post("/api/courses", json=new_course)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["success"] == True
    assert data["data"]["course_name"] == new_course["course_name"]

def test_update_course(client):
    updated_course = {
        "course_name": "CS Elective",
        "course_description": "computer theories."
    }
    response = client.put("/api/courses/200", json=updated_course)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_delete_course(client):
    response = client.delete("/api/courses/203")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

# Students Tests
def test_get_students(client):
    response = client.get("/api/students")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True
    
def test_get_student(client):
    response = client.get("/api/students/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_create_student(client):
    new_student = {
        "student_firstName": "John",
        "student_lastName": "Park",
        "student_email": "park@gmail.com",
        "student_password": "tghnbyfrew"
    }
    response = client.post("/api/students", json=new_student)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["success"] == True
    assert data["data"]["student_firstName"] == new_student["student_firstName"]

def test_update_student(client):
    updated_student = {
        "student_firstName": "Karen Angela",
        "student_lastName": "Realubit",
        "student_email": "nene@gmail.com",
        "student_password": "ftgbnutwqa"
    }
    response = client.put("/api/students/1", json=updated_student)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_delete_student(client):
    response = client.delete("/api/students/36")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

# --- Enrollments Tests ---
def test_get_enrollments(client):
    response = client.get("/api/enrollments")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_get_enrollments(client):
    response = client.get("/api/enrollments/100")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_create_enrollment(client):
    new_enrollment = {
        "student_id": 30,
        "course_id": 200,
        "enrollment_date": "2024-12-09",
        "completion_date": "2025-12-09"
    }
    response = client.post("/api/enrollments", json=new_enrollment)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["success"] == True

def test_update_enrollment(client):
    updated_enrollment = {
        "student_id": 11,
        "course_id": 200,
        "enrollment_date": "2024-12-10",
        "completion_date": "2026-12-10"
    }
    response = client.put("/api/enrollments/111", json=updated_enrollment)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_delete_enrollment(client):
    response = client.delete("/api/enrollments/130")  
    assert response.status_code == 403
    data = json.loads(response.data)
    assert data["success"] == False

# --- Test Results Tests ---
def test_get_test_results(client):
    response = client.get("/api/test_results")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_get_test_results(client):
    response = client.get("/api/test_results/301")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_create_test_result(client):
    new_test_result = {
        "student_id": 30,
        "test_score": 85,
        "test_date": "2024-12-09"
    }
    response = client.post("/api/test_results", json=new_test_result)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["success"] == True

def test_update_test_result(client):
    updated_test_result = {
        "student_id": 14,
        "test_score": 99,
        "test_date": "2022-12-02"
    }
    response = client.put("/api/test_results/314", json=updated_test_result)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] == True

def test_delete_test_result(client):
    response = client.delete("/api/test_results/330")  
    assert response.status_code == 403
    data = json.loads(response.data)
    assert data["success"] == False
