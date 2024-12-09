#import maths_operations
from maths_operations import *

exitCase = False
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
while(exitCase == False):
    UserInput = int(input("Select an arithmetic operation:\n1)Add \n2)Subtract \n3)Multiply \n4)Divide \n"))

    if UserInput == 1:
        result = add(first_num, second_num)
        print(result)
        exitCase = True
    elif UserInput == 2:
        result = subtract(first_num, second_num)
        print(result)
        exitCase = True
    elif UserInput == 3:
        result = multiply(first_num, second_num)
        print(result)
        exitCase = True
    elif UserInput == 4:
        result = divide(first_num, second_num)
        print(result)
        exitCase = True
    else:
        print("wrong input please try again")