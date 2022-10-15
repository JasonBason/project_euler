# Import new function first

import sys

sys.path.append("C:/Users/jshih/mu_code/project_euler/Functions")

from string_addition_scenario2 import add_2_strings

number = str(2**1000)
# print(len(number))

# Testcase
#number = str(2**15)

answer = "0"
for digit in number:
    answer = add_2_strings(answer, digit)

print(answer)