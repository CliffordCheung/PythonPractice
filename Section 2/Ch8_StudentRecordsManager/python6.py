student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return (False)
    else:
        if course in student_records[name]["courses"]:
            return (True)
        else:
            return (False)

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return (None)
    else:
        total_score = 0
        number = 0
        average_grade = 0.0
        if len(student_records[name]["grades"]) == 0:
            average_grade = 0
        else:
            for score in student_records[name]["grades"]:
                total_score += score
                number += 1
            average_grade = total_score / number
        return average_grade

def list_students_by_course(course):
    name_list = []
    for name in student_records:
        if is_enrolled(name,course):
            name_list.append(name)
    return name_list
    


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list