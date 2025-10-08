def transform_dataset(data):
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
    qualified_students = {
        student["student_id"]: round(sum(student["grades"]) / len(student["grades"]), 2)
        for student in data
        if all(grade > 70 for grade in student["grades"])
    }
    
    # Step 2: Create a summary of subjects taken by qualified students
    subject_summary = {}
    for student in data:
        if student["student_id"] in qualified_students:
            for subject in student["subjects"]:
                subject_summary[subject] = subject_summary.get(subject, 0) + 1
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary
    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary
    }
    

data = [{"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}]
result = transform_dataset(data)
print(result)