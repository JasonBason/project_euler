"""
How to add strings
5687586
8394893
xxx4579
"""

"""
1. Format the data to an array of numbers
2. Take the sum of the numbers in the array
"""


f = open("pe013.txt")
contents = f.read()
f.close()

formattedInput = contents.split('\n')
#print(formattedInput)


#int_formattedInput = []
#for number in formattedInput:
#  int_formattedInput.append(int(number))
#print(int_formattedInput)

sum = 0
for number in formattedInput:
  sum+= int(number)
print(sum)