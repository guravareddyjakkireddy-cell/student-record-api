from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
next_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Student Record Management REST API is running"}), 200


@app.route("/students", methods=["POST"])
def create_student():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not name or age is None or not course:
        return jsonify({"error": "Fields 'name', 'age', and 'course' are required"}), 400

    if not isinstance(age, int):
        return jsonify({"error": "'age' must be an integer"}), 400

    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    next_id += 1

    return jsonify({
        "message": "Student created successfully",
        "student": student
    }), 201


@app.route("/students", methods=["GET"])
def get_all_students():
    return jsonify(students), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if name is not None:
        student["name"] = name

    if age is not None:
        if not isinstance(age, int):
            return jsonify({"error": "'age' must be an integer"}), 400
        student["age"] = age

    if course is not None:
        student["course"] = course

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    }), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students

    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if s["id"] != student_id]

    return jsonify({"message": "Student deleted successfully"}), 200


@app.errorhandler(404)
def route_not_found(error):
    return jsonify({"error": "Route not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
