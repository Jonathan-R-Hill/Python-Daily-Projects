def prime(number):

    for i in range(2, number):
        
        is_prime = True
        if number % i == 0:
            is_prime = False
            break
        
    if is_prime == True:
        print(f"{number} is prime")
    
    else:
        print(f"{number} is not prime")
        
prime(number = 997)