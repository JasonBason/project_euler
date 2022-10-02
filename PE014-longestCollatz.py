"""
1. Iterate zero to a million with a for-loop
2. Define the two even/odd functions that define a Collatz sequence
3. Run each number from zero to a million through both functions until the ending number is 1
4. record infromation in 2d array: [starting number, length of Collatz Sequence]
"""


def even_function(num):
    return num / 2


def odd_function(num):
    return num * 3 + 1


collatz_list = []
for num in range(1, 1000000):
    starting_num = num
    counter = 0
    while num != 1:
        if num % 2 == 0:
            num = even_function(num)
            counter += 1
        elif num % 2 != 0:
            num = odd_function(num)
            counter += 1
    collatz_list.append([starting_num, counter])

collatz_list = sorted(collatz_list, key=lambda l: l[1])
print(collatz_list)

#837799 with 524 steps