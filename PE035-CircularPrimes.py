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

prime_boolean_array = (find_prime_number(100))

prime_numbers = []

for i in range(len(prime_boolean_array)):
    if prime_boolean_array[i] ==True:    
        prime_numbers.append(i)

# print(prime_numbers)

def number_rotator(number):
    number_array = ([*str(number)])
    print(number_array)
    


number_rotator(123)

def circular_prime_number(prime_numbers_array):
    for prime in prime_numbers_array:
        print('test')
        

        