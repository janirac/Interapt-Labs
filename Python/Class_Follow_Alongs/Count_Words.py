input_string = input("Enter a string ").lower()

count_dict = {}


for char in input_string:
    if char != " ":
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
        
for letter, count in count_dict.items():
    print(f'{letter} occurs {count} times')
        
