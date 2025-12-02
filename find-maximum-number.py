# write an algorithm that reads 3 numbers and then outputs the largest of the three.
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
if num1 > num2 and num1 > num3:
    print(f'The number {num1} is greater than {num2} y {num3}')
else:
    print(f'The number {num1} is less than {num2} y {num3}')
