# student-record-api
Student Record Management REST API using Flask
# Student Record Management REST API

## Project Overview
This mini project is a Python Flask-based REST API that performs CRUD operations for student records.

## Features
- Create a student
- Get all students
- Get a student by ID
- Update student details
- Delete a student
- Error handling for invalid requests and missing records

## Technology Stack
- Python
- Flask
- Postman

## Project Structure
student-record-api/
├── app.py
├── requirements.txt
├── README.md
├── postman_collection.json
└── .gitignore

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Server URL:
   ```
   http://127.0.0.1:5000
   ```

## API Endpoints
- `GET /`
- `POST /students`
- `GET /students`
- `GET /students/<id>`
- `PUT /students/<id>`
- `DELETE /students/<id>`

## Sample JSON for Create Student
```json
{
  "name": "John",
  "age": 23,
  "course": "Python"
}
```

## Postman
Import `postman_collection.json` into Postman and test all endpoints.

## GitHub Repository
Create a GitHub repository named `student-record-api` and upload these files.

