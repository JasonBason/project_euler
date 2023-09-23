"""
Design
1. Use is_prime to generate a boolean array for prime number identification
2. Begining with the first prime number (2), add prime numbers consecutively until the upper limit is reached. If the sum of the prime numbers is itself a prime number, flag the number and store the counter value.
3. Iterate through the next prime numbers
"""
upper_limit = 1000000
counter = 0
answer = 0


def is_prime(upper_limit):
    # Returns boolean array of size upper_limit that states if the number is prime or not
    starting_point = 2
    is_prime = [True] * upper_limit

    while starting_point < upper_limit:
        multiple = starting_point
        while multiple < upper_limit:
            multiple += starting_point
            if multiple < upper_limit:
                is_prime[multiple] = False
        starting_point += 1

    return is_prime


is_prime = is_prime(upper_limit)
# Manually convert 0 and 1 to prime numbers
is_prime[0] = False
is_prime[1] = False

#print(is_prime)

# Generate an array of prime numbers below the upper limit
primes_under_upperlimit = []
for number in range(len(is_prime)):
  if is_prime[number] == True:
    primes_under_upperlimit.append(number)

#print(primes_under_upperlimit)

starting_index = 0 

prime_number_counter_array = []

for index in range(len(primes_under_upperlimit)):
  # Add the next number
  current_index = starting_index
  #print(f"starting index: {starting_index}")
  sum = primes_under_upperlimit[current_index] 
  consecutive_prime_counter = 0
  while current_index < len(primes_under_upperlimit) - 1:
    sum += primes_under_upperlimit[current_index+1]
    current_index += 1
    consecutive_prime_counter+=1
    if sum in primes_under_upperlimit:
      prime_number_counter_array.append([sum, consecutive_prime_counter+1])
      #print(f"{sum} is a prime number with counter = {consecutive_prime_counter+1}")
    #print(f"current sum: {sum}")
  starting_index += 1
