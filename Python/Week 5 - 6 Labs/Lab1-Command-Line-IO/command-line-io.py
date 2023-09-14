import sys
# Part 1
my_name = input("Enter your name ==> ")
print(f'{my_name = }')
print(f'I am {my_name}')
print(f'I am \n\t{my_name}\nand I code for a living')

# Part 2
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print(f'Sum of {num1} and {num2} is {num1 + num2}')