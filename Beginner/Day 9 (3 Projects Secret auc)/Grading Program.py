student_scores = {
    "Harry" : 81,
    "Jenny" : 94,
    "Kanye" : 64,
    "Hilly" : 70,
    "Jonny" : 97,
    "Graham" : 76
}

student_grades = {}


for key in student_scores:
    
    value = student_scores[key]
    
    if value >= 91:
        student_grades[key] = "Outstanding"
    
    elif 70 <= value <= 90:
        student_grades[key] = "Acceptable"
    
    elif value < 70:
        student_grades[key] = "Fail"

print(student_grades)