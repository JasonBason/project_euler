PYTHAGOREAN_SUM_TOTAL = 12
#find all number where a<b<c that add up to PYTHAGOREAN SUM
# for num in range(0,PYTHAGOREAN_SUM+1):


# Use a while loop to iterate up to the PYTHAGOREAN SUM
# for each number, choose another number that is greater than the first
# for the third number, choose a number that is greater than the third
# check to see if the squares of numbers 1 and 2 equal to the square of three
# if this check checks out, then add it to a tupple and into a list
#
# i=0
# while i <= PYTHAGOREAN_SUM:
#     # if i%2 ==0:
#     #     print(i)
#     a = i
#
#     i+=1
def find_pythagorean_triplet(PYTHAGOREAN_SUM):
    for a in range(1,PYTHAGOREAN_SUM+1):
        for b in range(a, PYTHAGOREAN_SUM+1):
            for c in range(b,PYTHAGOREAN_SUM+1):
                if a**2 +b**2 == c**2 and a+b+c == PYTHAGOREAN_SUM:
                    return(a,b,c)

print(find_pythagorean_triplet(1000))