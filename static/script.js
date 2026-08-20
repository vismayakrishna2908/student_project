async function addStudent() {
    const name =
        document.getElementById("name").value;
    const age =
        document.getElementById("age").value;
    const grade =
        document.getElementById("grade").value;
    const blood_group =
        document.getElementById("blood_group").value;
    const course =
        document.getElementById("course").value;
    const response =
        await fetch(
            "/add_student",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify(
                    {
                        name: name,
                        age: age,
                        grade:grade,
                        blood_group:blood_group,
                        course: course
                    }
                )
            }
        );
    const data =
        await response.json();
    alert(data.message);
}
async function viewStudents() {
    const response =
        await fetch("/get_students");
    const students =
        await response.json();
    const list =
        document.getElementById(
            "studentList"
        );
    list.innerHTML = "";
    students.forEach(
        function(student) {
            const item =
                document.createElement("li");
            item.textContent =
                student[1] +
                " | Age: " +
                student[2] +
                " | Grade: " +
                student[3] +
                " | blood_group:"+
                student[4]+
                " | Course:"
                student[5]+

            list.appendChild(item);
        }
    );
}