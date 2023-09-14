#  part 1

num1 = 100
num2 = 2.71828
num3 = 3.14159
num4 = 200

print(f'{num1} times {num2} = {num1 * num2}')
print(f'{num1} divided by {num2} = {num1 / num2}')
print(f'{num2} raised to the power of {num3} is {num2 ** num3:.6f}')
print(f'{num1} plus {num4} THEN multiplied by {num2} is {(num1 + num4) * num2:.3f}')
print(f'{num1} plus {num4} THEN divided by {num2} plus {num3} is {((num1 + num4) / (num2 + num3))}')
print(f'{num1} divided by {num2} plus {num4} divided by {num3} {(num1 / num2) + (num4 / num3)}')
print()
print(f'Is {num1} less than {num4} {num1 < num4}')
print(f'Is {num1} greater than {num2} OR {num3} equal to 200? {num1 > num2 or num3 == 200}')
print(f'Is {num1} cubed greater than {num4} squared? {num1 ** 3 > num4 **2}')
print(f'Is true greater than false {True > False}')
print()
print(f'The letter "f" in "abcdef" {"f" in "abcdef"}')
print(f'The letter "k" is not in "abcdef" {"k" not in "abcdef"}')
print()
print(f'{num1} equals 100.0? {num1 == 100.0}')
print(f'{num1} is the same object as 100.0? {id(num1) == id(100.0)}')

# part 2

user_input = (int(input("Enter a temp ")))
print(f'{user_input} C to F is {((9 * user_input) / 5) + 32} F')