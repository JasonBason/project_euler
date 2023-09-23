def sum_squares(last_number):
    list_squares = [num**2 for num in range(1,last_number+1)]
    return sum(list_squares)

print(sum_squares(10))

def square_sum(last_number):
    return sum(range(0,last_number+1))**2

print(square_sum(10))

print(square_sum(100)-sum_squares(100))