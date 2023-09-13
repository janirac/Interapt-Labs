import time
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

def number_check(num):
    if num in range(1, 10):
        print(f"{num} is in the range 1 - 10")
    else:
        print(f"{num} is not in the range")
        
# print(number_check(5))


def upper_and_lower_count(string):
    upper = 0
    lower = 0
    for char in string:
        if char != " ":
            if char.isupper():
                upper += 1
            else:
                lower += 1
            
    print(f"No. of Upper case characters: {upper}")
    print(f"No. of Lower case characters: {lower}")
    
# print(upper_and_lower_count("The quick Brow Fox"))

def distinct_list(list):
    new_list = []
    
    for ele in list:
        if ele not in new_list:
            new_list.append(ele)
            
    print(new_list)
    
# print(distinct_list([1,2,3,3,3,3,4,5]))

def prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

# print(prime(2))
# print(prime(1))
# print(prime(4))
# print(prime(5))

def find_even(list):
    even_list = [num for num in list if num % 2 == 0]
    return even_list

# print(find_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def perfect_number(number):
    list_of_factors = []
    total_of_factors = 0
    
    for factor in range(1, number):
        if number % factor == 0:
            total_of_factors += factor
            list_of_factors.append(factor)
            
    print("----------")
    print(list_of_factors)
    print(total_of_factors)
    
    
    if total_of_factors == number: 
        return True
    else:
        return False
            
    

# print(perfect_number(6)) #True
# print(perfect_number(2)) #False
# print(perfect_number(28)) #True
# print(perfect_number(13)) #False

def palindrome(string):
    reverse_string = string[::-1]
    return reverse_string == string
    
# print(palindrome("madam"))
# print(palindrome("no"))
# print(palindrome("non"))
# print(palindrome("nurses"))

def pascals_triangle(n):
    triangle = [1]
    
    for i in range(n):  # This is how many times I will do it 
        print(triangle)  # This will print the current triangle
        
        temp = [1] #temp to keep track of triangle without modifying
        
        for num in range(1, len(triangle)): 
            new_element = triangle[num - 1] + (triangle[num] if num < len(triangle) else 0)
            temp.append(new_element)
        
        temp.append(1) 
        triangle = temp  
        
pascals_triangle(4)

def pangram(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alpha:
        if char not in string:
            return False
        
    return True

# print(pangram("The quick brown fox jumps over the lazy dog"))
# print(pangram("dog"))

def hyphen_sorted_sentence(string):
    return "-".join(sorted(string.split("-")))

# print(hyphen_sorted_sentence("green-red-yellow-black-white"))

def squared():
    squared_numbers  = [num ** 2 for num in range(1, 21)]
    return squared_numbers

# print(squared())

def python_code(string):
    exec(string)

# print(python_code('print("hello world")'))

def outer_function():
    def inner_function():
        print("Im inside the inner function")
        
    return inner_function()

# print(outer_function())

def count_number_of_local_variables():
    var1 = "var1"
    var2 = "var1"
    var3 = "var1"
# print(count_number_of_local_variables.__code__.co_nlocals)

def miliseconds(n):
    print("starting")
    time.sleep(n)
    print("program now printing")
    print(squared())

# print(miliseconds(3))

        