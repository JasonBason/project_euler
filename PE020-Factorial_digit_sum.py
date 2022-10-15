# Factorial digit sum
# Problem 20

import sys

sys.path.append("C:/Users/jshih/mu_code/project_euler/Functions")
          
from string_addition_scenario2 import add_2_strings 
    
def factorial(number):
    "Obtain the factorial product given a single number"
    factorial_product = 1
    for num in range(number):
        factorial_product *= (num+1)
    return factorial_product


def add_digits(number):
    "Use the add_2_strings function to add digits together"
    "number variable must be a string"
    sum_digits = "0"
    for num in number:
        sum_digits = add_2_strings(sum_digits, num)    
    return sum_digits
        
print(add_digits("20"))

print(add_digits(str(factorial(100))))