import json
import student
def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            Students = []

            for info in data:
                student_obj = student.Student.from_dict(info)
                Students.append(student_obj)

            return Students

    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []
def save_students(Students):
    data = []
    for student in Students :
        data.append(student.to_dict())
    with open ("students.json","w") as file :
        json.dump(data,file,indent = 4)