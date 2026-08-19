from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def create_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """)

    connection.commit()
    connection.close()
create_database()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/add_student", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data["name"]
    age = data["age"]
    course = data["course"]

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students(name, age, course)
        VALUES(?,?,?)
        """,
        (name, age, course)
    )

    connection.commit()

    connection.close()

    return jsonify(
        {
            "message": "Student added successfully"
        }
    )


@app.route("/get_students")
def get_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    connection.close()

    return jsonify(students)


if __name__ == "__main__":

    app.run(debug=True)