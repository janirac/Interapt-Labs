# part 1

letter_a = "A"
three_spaces = "   "
print(f'{letter_a: ^38}')
print(f'{letter_a: >17}{three_spaces}{letter_a:<17}')
print(f'{letter_a: >16}',end="" )
print(f'{letter_a}{letter_a}{letter_a}{letter_a}{letter_a}{letter_a:<15}' )
print(f'{letter_a: >15}{three_spaces:>7}{letter_a:<15}')
print(f'{letter_a: >14}{three_spaces:>9}{letter_a:<14}')

# part 2 

num1 = 100
num2 = 3.14159

print(f'{num1} multiplied by {num2} = {num1 * num2:.5f}')
print(f'The type of {num1} is {type(num1)}')
print(f'The type of {num2} is {type(num2)}')
print( f'The unique object identifier of {num1} is {id( num1 ) }')
print( f'The unique object identifier of {num2} is {id( num2 ) }')

# part 3

string1 = "Hello"
string2 = "Hello"
print(f'{id(string1) = }\t\t{id(string2) = }')

string1 += " There"
string2 += " There"
print(f'{id(string1) = }\t\t{id(string2) = }')

num1 = 10
num2 = 10.0
print(f'{id(num1) = }\t\t{id(num2) = }')

num1 += 100
num2 -= 5
print(f'{id(num1) = }\t\t{id(num2) = }')


