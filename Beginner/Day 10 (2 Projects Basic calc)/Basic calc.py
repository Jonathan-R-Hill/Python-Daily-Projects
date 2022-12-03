def calc(num1, num2, sign):
    
    if sign == "+":
        answer = num1 + num2
    elif sign == "-":
        answer = num1 - num2
    elif sign == "*":
        answer = num1 * num2
    elif sign == "/":
        answer = num1 / num2
    else:
        answer = "Invalid input"
    
    return answer

def carryon(num):
    global answer
    global play
    
    check = input(f"Carry on with the number: {num}   Y or N\n").capitalize()
    
    if check == "Y":
        num1 = num
        sign = input("Enter your sign:\n+\n-\n*\n/\n")
        num2 = float(input("Enter the second number:  "))
        
        answer = calc(num1 = num1, sign = sign, num2 = num2)
        
    else:
        play = False
        
  
play = True
num1 = float(input("Enter the first number:  "))
sign = input("Enter your sign:\n+\n-\n*\n/\nYour sign:  ")
num2 = float(input("Enter the second number:  "))
calc(num1 = num1, sign = sign, num2 = num2)
answer = calc(num1 = num1, sign = sign, num2 = num2)

while play == True:
    
    print(answer)
    carryon(num = answer)
    