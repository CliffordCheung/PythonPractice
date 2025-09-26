def analyze_grades(grades):
    # Write code here
    total = 0
    number = 0
    highest = 0
    lowest = 100
    average = 0    
    
    for name in student_grades:
        total += student_grades[name]
        number +=1
        if student_grades[name]> highest:
            highest = student_grades[name]
            top_student = name
        if student_grades[name] < lowest:
            lowest = student_grades[name]
            bottom_student = name
    average = total/number
    ans_list = {"average": average, "highest": highest, "lowest": lowest, "top_student": top_student, "bottom_student":bottom_student }
    # return(total/number)
    return(ans_list)

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)