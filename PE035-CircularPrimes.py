upper_limit = 1000000
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

prime_boolean_array = (find_prime_number(upper_limit))

prime_dic = dict(zip(list(range(0,upper_limit)),prime_boolean_array))
prime_dic[0] = False
prime_dic[1] = False
#print(prime_dic)



def number_rotator(number):
    rotatable = False
    for rotation in range(len(str(number))):
        number = str(number)[1:] + str(number)[0]
        print(number)
        if prime_dic[int(number)] == True:
            rotatable = True
        else:
            rotatable = False
            break
    return rotatable
(number_rotator(101))
(number_rotator(13))


rotatable_prime_list = []

def circular_prime_number(prime_numbers_array):
    for number, prime_status in prime_numbers_array.items():
        if prime_status == True:
            if number_rotator(number) == True:
                rotatable_prime_list.append(number)

circular_prime_number(prime_dic)        

print(rotatable_prime_list)   
print(len(rotatable_prime_list))  