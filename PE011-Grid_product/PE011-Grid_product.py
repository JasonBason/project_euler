# 1) read file into a 2d list
# 2) define left to right function to calculate 4 chunk products
# 3) Calculate vertical maximum for 4 chunks
# 4) Calculate diagonals for 4 chunks
# 5) Calculate all possible products

f = open("pe011-test.txt")
contents = f.read()
f.close()

rows = (contents.split('\n'))

matrix = []
for row in rows:
    matrix.append([int(num) for num in row.split(' ')])


def product_of_four(list_of_four):
    product = 1
    for num in list_of_four:
        product *= num
    return product


def horizontal_row_product(row):
    product_array = []
    first_number = 0
    second_number = 1
    third_number = 2
    fourth_number = 3

    while fourth_number < len(row):
        multiplicants = [
            row[first_number], row[second_number], row[third_number],
            row[fourth_number]
        ]
        first_number += 1
        second_number += 1
        third_number += 1
        fourth_number += 1
        product_array.append(product_of_four(multiplicants))
        print(product_array)
    return max(product_array)


def horizontal_matrix(matrix):
    product_array = []
    for row in matrix:
        product_array.append(horizontal_row_product(row))
    print(f'product_array is: {product_array}')
    return max(product_array)


print(f'\nanswer is {horizontal_matrix(matrix)}')

# Vertical
# Purpose: Make a function that will calculate the vertical products of four numbers

print("Vertical")
# matrix[x][y]
four_adajcent_nums = 4
starting_row_index = 0
# [0][0]
# [1][0]
# [2][0]
# [3][0]

# [1][0]
# [2][0]
# [3][0]
# [4][0]

# [0][1]
# [1][1]
# [2][1]
# [3][1]

# while starting_row_index < four_adajcent_nums:
#   arr.push(row[starting_row_index][y])
#   starting_row_index += 1

for row in matrix:
    print(row)


def vertical_column_product(matrix):
    row = 0
    while row < len(matrix):
      print(matrix[row])
      row += 1
      


#vertical_column_product(matrix)