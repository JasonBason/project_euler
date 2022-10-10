'''
1. split string to 

scenario 1:
-11-
-456
-789
----
1245

scenario 2:
897
--6
---
str2[1] = undefined

int(str1[counter])  
'''


def add_2_strings(str1, str2):
    counter = len(str1) - 1
    answer = ''
    carry = 0
    while counter >= 0:
        digit1 = int(str1[counter])
        digit2 = int(str2[counter])
        digit_sum = str(digit1 + digit2 + carry)
        digit = digit_sum[1] if len(digit_sum) > 1 else digit_sum[0]
        carry = int(digit_sum[0]) if len(digit_sum) > 1 else 0
        answer = digit + answer
        counter -= 1
    answer = str(carry) + answer if carry !=0 else answer
    return answer


print(add_2_strings("123", "123"))
print(add_2_strings("456", "789"))
