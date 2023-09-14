# part 1

found = False
max_num_of_guesses = 5
num_to_guess = 45

while input("Wanna play the number guessin game? (y or n) ==> ").upper() == "Y":
    found = False
    max_num_of_guesses = 5
    num_to_guess = 45
    while( not found and max_num_of_guesses > 0 ):
        guess = int(input(f'Enter a number between 1 and 100 ==> '))
        if guess == num_to_guess:
            print(f'You found the number {num_to_guess}!\n And it took you {5-max_num_of_guesses} tries to find it')
            found = True
        elif 0 < guess < 100:
            print(f'{guess} is too {"low" if guess < num_to_guess else "high"}')
            max_num_of_guesses -= 1
        else:
            print(f"{guess} is an invalid entry... try again\n")
            
#  part 2
to_continue = True
while to_continue:
    options = input('Enter:\n\tC to create, \n\tR to read, \n\tU to update, \n\tD to delete, \n\tQ to quit ==> ').upper()
    if options == "C":
        print("Calling CREATE routine.....")
    elif options == "R":
        print("Calling READ routine.....")
    elif options == "U":
        print("Calling UPDATE routine.....")
    elif options == "D":
        print("Calling DELETE routine.....")
    elif options == "Q":
        print("Exiting program")
        to_continue = False
    else:
        print(f"Your entry {options} is invalid - try again")
    
        