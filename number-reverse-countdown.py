# Code a subprogram that prints the countdown starting from a number entered by the user.
def countdown (n): 
    if n == 0: # we say that if n is 0, then there won't be any countdown
        print(n)
    else: # if n ≠ 0, countdown happens
        print(n)
        countdown (n - 1)

n = int(input('Enter a number: '))
countdown(n)
