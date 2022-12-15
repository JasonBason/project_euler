# p022
# Design
# 1. Sort names into alphabetical order
# 2. Determine alphabetical value of name where A=1, B=2, C=3 etc.
# 3. Multiply alphabetical value by the index number of the name to find the score
# 4. Find the sum of all names in txt file
'''
read in file as a 1D array
Sort names array in alphabetical order using sort function
Determine alphabetical value of a name by iterating through the characters of a name and assigning each character a number with a for loop, using a dictionary
Take the product of all assigned characters and multiply this by the index number of the name
Use for loop to assign values to all names
'''


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
"""
alphabet_dictionary = dict(zip((alphabet), range(len(alphabet))))
"""

answer = alphabet.index("A")

with open("p022_names.txt") as file:
  names = file.read()
names = names.split(",")

names = [name.strip('\"') for name in names]
names = sorted(names)
print(names[0])
print(names[-1])

#print(names)

def alphabetical_value(name):
  character_sum = 0
  for character in name:
    #print(character)
    character_sum += alphabet.index(character)+1
    #print(character_sum)
  return character_sum

#Iterate through the names
answer = 0
for name_index in range(len(names)):
  answer += (name_index+1)*alphabetical_value(names[name_index])  
print(answer)

alphabetical_value(names[0])
print(alphabetical_value('COLIN'))


