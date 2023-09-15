def enter_float_in_range( prompt, low, high ):
    while True:
        try:
            user_input = float(input(prompt))
            if low <= user_input <= high:
                return user_input
            else:
                print(f'Value entered is not in range {low} and {high}. Try again')
        except ValueError:
            print("Value entered is not an float. try again")
        
def enter_integer_in_range(prompt, low, high):
    while True:
        try:
            user_input = int(input(prompt))
            if low <= user_input <= high:
                return user_input
            else:
                print(f'Value entered is not in range {low} and {high}. Try again')
        except ValueError:
            print("Value entered is not an int. try again")
        
def enter_an_integer(prompt):
    while True:
        try:
            user_input = int((input(prompt)))
            return user_input
        except ValueError:
            print("Value entered is not an int. try again")
            
def enter_a_float(prompt):
    while True:
        try:
            user_input = float((input(prompt)))
            return user_input
        except ValueError:
            print("Value entered is not an float. try again")
            
def main():
    print(enter_integer_in_range("Enter integer between 1 and 5 ", 1, 5))
    print()
    print(enter_float_in_range("Enter float between 1.5 and 5.5 ", 1.5, 5.5))
    print()
    print(enter_an_integer("Enter integer => "))
    print()
    print(enter_a_float("Enter float => "))
    
    
    
print(main())