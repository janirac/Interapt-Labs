# part 1
from getty import abe_talking
from string import ascii_lowercase

def remove_punctuation(string):
    punct_chars = "\"'.,?!-_"
    punct_chars_removed = string
    for punct_char in punct_chars:
        punct_chars_removed = punct_chars_removed.replace(punct_char, "")
        
    return punct_chars_removed

def count_dictionary(lowercase_or_words, string_or_list):
    dictionary = {}
    for string in lowercase_or_words:
        dictionary[string] = string_or_list.count(string)
        
    return dictionary

def print_table(headers,lowercase_or_words, abe_talking_as_string_or_list):
    the_dictionary = count_dictionary(lowercase_or_words, abe_talking_as_string_or_list)
    print(f'{headers[0]:<20}{headers[1]:>30}')
    for key, value in the_dictionary.items():
        print(f'{key:<20}{value:>30}')
    
getty_no_punct = remove_punctuation(abe_talking)
getty_no_punct_list = getty_no_punct.split()
unique_address_words = sorted( { a_word.lower() for a_word in getty_no_punct_list } )

# print(print_table(["Letter", "Count"], ascii_lowercase, getty_no_punct))
# print(print_table(["Word", "Count"], unique_address_words, getty_no_punct_list))

# part 2
def print_first_n_set_values(set_tb_printed, num_to_print):
    for ele in range(0, num_to_print):
        print(set_tb_printed[ele])
    
def print_first_n_list_values(list_tb_printed, num_to_print):
    for ele in range(0, num_to_print):
        print(list_tb_printed[ele])
    
def print_first_n_dict_values(dict_tb_printed, num_to_print):
    for ele in range(0, num_to_print):
        print(dict_tb_printed[ele])
    
def print_first_n_values( structure_tb_printed, num_to_print='all' ):
    if num_to_print == 'all':
        num_to_print = len( structure_tb_printed )
    # Set up dictionary to call appropriate function
    # based on the data type of the structure
    #
    # Accessing set elements same as accessing list elements;
    # Use same function for both
    dict_for_print_structures = { type(list()) :print_first_n_list_values,
                                  type(dict()) :print_first_n_dict_values,
                                  type(set())  :print_first_n_set_values,
                                }
    # call the appropriate helper function
    if type(structure_tb_printed ) in dict_for_print_structures:
       dict_for_print_structures[ type( structure_tb_printed )](structure_tb_printed, num_to_print )
    else:
        print( f'{type(structure_tb_printed)} has no special print function')
        
def main():
   a_list = [1, 2, 'a', 'b', 4.5, '5']
   a_set = {1, 2, 'd', 'll', 23}
   a_dict = { 1: "a", 2: "BB", 3: "cc", "X": "Some text"}
   a_tuple = (1, 'a', 3)

   list_o_structs = [ a_list, a_set, a_dict, a_tuple ]
   for a_struct in list_o_structs:
       print_first_n_values( a_struct, 3 )
   list_o_structs = [ a_list, a_set, a_dict, a_tuple ]
   for a_struct in list_o_structs:
       print_first_n_values( a_struct )
