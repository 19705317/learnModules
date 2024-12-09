import sys
from sys import *

#take all args
arguments = argv[0:]

if len(sys.argv) > 1:
    print(f"This is the name of the program: {arguments[0]}")
    print(f"Number of arguments passed: {len(arguments)}")
    print(f"Arguments list: {arguments}")
    for element in arguments:
        print(element)
else:
    print("Error: no arguments passed")

