# Write a Python function to find the maximum of three numbers 
example_list = [8, 2, 3, -1, 7]

def maximum(example_list):
    max_num = max(example_list)
    
    return max_num
    
# print(maximum(1, 2, 3))

# Write a function to sum all the numbers in a list

def sum_of_list(list):
    return sum(list)

# print(sum_of_list(example_list))


# Write a function to multiply all the numbers in a list

def multiply_list(example_list):
    product = 1
    for factor in example_list:
        product *= factor
        
    return product

# print(multiply_list(example_list))


def reverse_string(string):
    reversed_string = ""
    
    i = len(string) - 1
    print(i)
    while i > -1:
        reversed_string += string[i]
        
        i -= 1
    return reversed_string

# print(reverse_string("1234abcd"))


def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
        
    return product
        
        
# print(factorial(4))

def 