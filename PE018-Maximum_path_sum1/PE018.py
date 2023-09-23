# Read in data as arrays

with open("pe018-data.txt") as file_object:
    contents = file_object.read()

rows = (contents.split("\n"))

triangle = []
for row in rows:
    triangle.append(list(map(int, row.split(" "))))




row_counter = len(triangle) - 1
firstRow = 0
optimal_paths = []

while row_counter > firstRow:
    # Step 1: finding the maximum between pairs
    counter = 0
    print(f"row_counter = {row_counter}")
    # current_row = triangle[row_counter]
    if row_counter == len(triangle) - 1:
        current_row = triangle[row_counter]
    else:
        current_row = optimal_path_sum
    #current_row = triangle[row_counter] if row_counter == len(triangle) - 1 else optimal_path
    # print(optimal_path==None)
    optimal_path = []
    while counter < len(current_row) - 1:
        larger_number = current_row[counter] if current_row[
            counter] > current_row[counter + 1] else current_row[counter + 1]
        optimal_path.append(larger_number)
        counter += 1
    print(f"current row: {current_row}")
    print(f"optimal_path is {optimal_path}")
    print(f"triangle[row_counter-1]: {triangle[row_counter-1]}\n")
    optimal_path_sum = [x + y for x, y in zip(optimal_path, triangle[row_counter - 1])]
    optimal_paths.append(optimal_path_sum)
    row_counter -= 1

print(optimal_paths)
