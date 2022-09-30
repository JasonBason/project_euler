# 1) read file into a 2d list
# 2) define left to right function to calculate 4 chunk products
# 3) Calculate vertical maximum for 4 chunks
# 4) Calculate diagonals for 4 chunks
# 5) Calculate all possible products

f = open("pe011.txt")
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
    """Identifies the 4 multiplicants and determines their product for each row"""
    
    
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
        #print(product_array)
    return max(product_array)


def horizontal_matrix(matrix):
    product_array = []
    for row in matrix:
        product_array.append(horizontal_row_product(row))
    #print(f'product_array is: {product_array}')
    return max(product_array)


print('horizontal is:') 
print(horizontal_matrix(matrix))

# Vertical
# Purpose: Make a function that will calculate the vertical products of four numbers

# print("Vertical")
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
NUMBERS_TO_MULTIPLY = 4

def vertical_column_product(matrix):
    product_array = []  
    for col_index in range(len(matrix[0])):       
        starting_row_index = 0
        ending_row_index = starting_row_index + NUMBERS_TO_MULTIPLY
        #print(f"\ncol_index: {col_index}")
        while ending_row_index < len(matrix)+1:
            multiplicants = []
            # print(f"starting number is {matrix[starting_row_index][col_index]}")
            # print(f"The range is: {starting_row_index}, {ending_row_index}")
            for number in range(starting_row_index,ending_row_index):
                multiplicants.append(matrix[number][col_index])
            #print(multiplicants)
            product_array.append(product_of_four(multiplicants))
            starting_row_index +=1
            ending_row_index +=1
    return(max(product_array))

print("vertical is:")
print(vertical_column_product(matrix))
            
#TODO: should I make the function modular like the horizontal function and then
# make a second function to got column by column?


# Strategy: define a starting number and then choose the next three numbers off of that
# If any number is extends out of range, then move on to the next number
def upleft_to_bottomright_product(matrix):
    product_array = []
    for row_index in range(len(matrix[0])):
        for col_index in range(len(matrix)):
            multiplicants = []
            for number in range(NUMBERS_TO_MULTIPLY):   
                   row = row_index + number
                   col = col_index + number
                   # print(f"row is {row}")
                   # print(f"col is {col}")
                   if row < len(matrix) and col < len(matrix[0]):
                       multiplicants.append(matrix[row][col])
                   else:
                       pass
            if len(multiplicants) == NUMBERS_TO_MULTIPLY:
                product_array.append(product_of_four(multiplicants))
                # print(multiplicants)
    return(max(product_array))

print("upleft is:")    
print(upleft_to_bottomright_product(matrix))



def bottomleft_to_upright_product(matrix):
    product_array = []
    for row_index in range(len(matrix[0])):
        for col_index in range(len(matrix)):
            multiplicants = []
            for number in range(NUMBERS_TO_MULTIPLY):   
                   row = row_index - number
                   col = col_index + number
                   #print(f"row is {row}")
                   # print(f"col is {col}")
                   if row >= 0 and col < len(matrix[0]):
                       multiplicants.append(matrix[row][col])
                   else:
                       pass
            if len(multiplicants) == NUMBERS_TO_MULTIPLY:
                product_array.append(product_of_four(multiplicants))
                #print(multiplicants)
    return(max(product_array))

print("bottomleft is:")
print(bottomleft_to_upright_product(matrix))