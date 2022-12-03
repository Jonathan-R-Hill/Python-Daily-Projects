import math

def calc(height, width, coverage):

    answer = math.ceil((height * width) / coverage)
    
    print(f"You will need {answer} cans of paint to cover the wall.")

calc(height = 7, width = 9, coverage = 6.00)
