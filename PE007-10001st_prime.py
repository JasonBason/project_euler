upper_limit = 1000000
desired_prime = 10003
counter = 0

def find_prime_number(upper_limit):
  starting_point = 2
  is_prime = [True]*upper_limit

  while starting_point < upper_limit:
    multiple = starting_point
    while multiple < upper_limit:
      multiple += starting_point
      if multiple < upper_limit:
        is_prime[multiple] = False
    starting_point += 1

  return is_prime

is_prime = find_prime_number(upper_limit)
print('check')

for index in range(len(is_prime)):
  if is_prime[index] == True:
    counter+=1
    if counter == desired_prime:
      print(index)
    else:
      pass

    