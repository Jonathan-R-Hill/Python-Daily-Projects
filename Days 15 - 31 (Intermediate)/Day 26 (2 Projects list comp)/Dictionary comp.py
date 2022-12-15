# new_dict = {New_key:New_value for (key, value) in dict.items() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_studetns = {key:value for (key, value) in student_scores.items() if value > 60}
print(passed_studetns)