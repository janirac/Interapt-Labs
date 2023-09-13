numbers = set()

while True:
    user_input = input("Enter a number or press Enter to finish => ")
    if user_input == "":
        break
    else:
        numbers.add(int(user_input))
        
if numbers:
    
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
    print(f"The total sum is: {total}")
    print(f"The average is: {average:.2f}")
else:
    print("There are no numbers")