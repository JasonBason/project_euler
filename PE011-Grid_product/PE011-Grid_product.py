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
    print(f"product: {product}")
    return product


def left_to_right_row_product(row):
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
      print(row[fourth_number])
      first_number += 1
      second_number += 1
      third_number += 1
      fourth_number += 1
      product_array.append(product_of_four(multiplicants))
      print(multiplicants)
    return max(product_array)


def left_to_right_matrix(matrix):
  for row in matrix:
      product_array = []
      product_array.append(left_to_right_row_product(row))
  print(f'product_array is: {product_array}')
  return max(product_array)


print(f'\nanswer is {left_to_right_matrix(matrix)}')
