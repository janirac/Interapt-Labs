# Replace several characters in a string with other characters
# E.G. Replace "a" with "AA", "e" with "EE", "i" with "II"

# This string:
# 'This is just a string with chars to be replaced'

# becomes:
# 'Th  II  s   II  s just   AA   str  II  ng w  II  th ch  AA  rs to b  EE   r  EE  pl  AA  c  EE  d'

# When 'i' is replaced by '  II  ', 'e' is replaced by '  EE  ', 'a' is replaced by '  AA  '
# 
# # for example
string_to_replace = 'This is just a string with chars to be replaced'

def replace_chars(string):
    new_string = string.replace('a', " AA ")
    new_string = new_string.replace('e', " EE ")
    new_string = new_string.replace('i', " II ")
    
    return new_string
            
            
print(replace_chars(string_to_replace))
