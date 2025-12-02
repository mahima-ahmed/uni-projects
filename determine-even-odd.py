# Enter a number through the keyboard and determine whether it is even or odd.
num = int(input('Enter a number: ')) # we use int so that the number results in an integer
if num % 2 == 0: # n is divided by 2 and if the remainder is 0, it is even
    print ('The generated number', num, 'is even.')
else:
    print ('The generated number', num, 'is odd')
# Basically, the result depends on the number we introduce; in this way, the code will interpret it as even or odd, depending on the condition that is met.
