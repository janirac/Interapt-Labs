import random

# part 1
def find_common_unique_elements( iter1, iter2 ):
    return list(set(iter1) & set(iter2))
    
iter1 = [1, 2, 3, 4, 5, 5, 8, 1]
iter2 = [1, 2, 2, 4, 5, 5, 7, 1]

# print(find_common_unique_elements(iter1, iter2))

def gen_return_random_unique_number_list():
   return list({random.randint(0, 20) for _ in range(0, 5)})

# print(gen_return_random_unique_number_list())

# part 2

from string import ascii_lowercase
from getty import abe_talking

punct_chars = "\"'.,?!-_"
abe_no_punct = abe_talking
for punct_char in punct_chars:
    abe_no_punct = abe_no_punct.replace(punct_char, "")

abe_no_punct_list = abe_no_punct.split()

unique_words = sorted({word.lower() for word in abe_no_punct_list})

word_count_table = {word: abe_no_punct_list.count(word) for word in unique_words}

print(f'{"Word":<20}{"Count":>30}')
for word, word_count in word_count_table.items():
    print(f'{word:<20}{word_count:>30}')
    
print()
print()
print()
print()
letter_count_table = {letter: abe_no_punct.count(letter) for letter in ascii_lowercase}

print(f'{"Word":<20}{"Count":>30}')
for letter, letter_count in letter_count_table.items():
    print(f'{letter:<20}{letter_count:>30}')



    
    