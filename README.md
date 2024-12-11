# Project Title
E LEARNING API

## Description
This data model ensures that all core processes of an e-learning platform are efficiently handled, providing robust user and course management, seamless enrollment tracking, and actionable reporting.


```cmd
# Installation
Flask==3.1.0
Flask-Bcrypt==0.7.1
mysql-connector-python==8.2.0
PyJWT==2.7.0
pytest==8.3.3
pytest-mock==3.10.0
python==3.12.3

# Configuration
DATABASE_URL: The URL for the database connection.

# API Endpoints (markdown table)
Endpoint	                   Method	 	   Description
======================================================================================================================
/api/students	                   GET		           List of students
/api/students/{id}	           GET		           Specific student
/api/students                      POST                    Create new student
/api/students/{id}                 PUT                     Update the existing student
/api/students/{id}                 DELETE                  Delete a student
/api/courses	                   GET		           List of courses
/api/courses/{id} 	           GET		           Specific course
/api/courses                       POST                    Create new course
/api/courses/{id}                  PUT                     Update the existing course
/api/courses/{id}                  DELETE                  Delete a course
/api/enrollments	           GET		           List of enrollment transaction
/api/enrollments/{id}              GET		           Specific enrollment transaction
/api/enrollments                   POST                    Create new enrollment transaction
/api/enrollments/{id}              PUT                     Update the existing enrollment transaction
/api/test_results	           GET		           List oftest_results
/api/test_results/{id}             GET		           Specific test_results
/api/test_results                  POST                    Create new test_results
/api/test_results/{id}             PUT                     Update the existing test_results

# Testing
-- Ensure that necessary dependencies installed, including pytest and any test-related libraries.
-- Ensure that the database and environment variables are set.
-- Go to the path of the file.
-- Start your testing.

# Git Commit Guidelines
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user tests
