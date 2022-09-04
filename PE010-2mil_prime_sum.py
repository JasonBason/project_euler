upper_limit = 2000000
counter = 0
answer = 0

def find_prime_number(upper_limit):
  # Returns boolean array of size upper_limit that states if the number is prime or not
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


def prime_summer(prime_array, counter, answer):
  for bool in range(len(prime_array)):
    if prime_array[bool] == True:
      answer+= counter
      print(counter)
    counter+=1

  return answer




is_prime = find_prime_number(upper_limit)
print(prime_summer(is_prime, counter, answer) - 1)