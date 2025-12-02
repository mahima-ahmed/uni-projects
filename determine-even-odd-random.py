# determine if a random number from 1 to 10 is even or odd, using the Python library
import random
n = random.randint (1,10) # a random number between 1 and 10
print (n)
if (n%2 == 0): # n is divided by 2 and if the remainder is 0, it is even
   print ('The generated number (%s) is even.' %n)
else : # if that condition is not met, then it is odd.
   print ('The generated number (%s) is odd.' %n)
# Everytime you run this code, it will generate different numbers between 1 and 10, and determine if it's even or odd.
