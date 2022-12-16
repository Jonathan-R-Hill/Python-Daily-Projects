def add(*nums): # tuple
    print(*nums)
    print(sum(nums))


def calculate(n, **kwargs):    # dict
    n += kwargs["add"]
    n *= kwargs["multiply"]
    
    print(n)
    

class Car:
    def __init__(self, **kw):
        self.make = kw["make"] # will return erro if not specified
        self.model = kw.get("model") # if not in kwargs will retrun none

my_car = Car(make = "Skoda", model = "Citigo")