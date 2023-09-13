from random import randint

num_in_list = int(input("Enter a number between 10 and 20 ==> "))

list_1 = [randint(1, num_in_list) for i in range(num_in_list) ]
list_2 = [randint(1, num_in_list) for i in range(num_in_list) ]

print(f"{list_1}\n{list_2}")

common_elems = []

for ele in list_1:
    if ele in list_2 and ele not in common_elems:
        common_elems.append(ele)
    
print(f"{common_elems}")

