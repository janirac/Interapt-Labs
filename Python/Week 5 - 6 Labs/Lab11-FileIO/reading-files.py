from string import punctuation
import os

abe_file = "abespeech.txt"
abe_rearranged = "abrrearranged.txt"


def remove_punctuation(line: str) -> str:
    return line.translate(str.maketrans(punctuation, ' ' * len(punctuation)))

def rearrange_line(line: str) -> str:
    line_no_punct = remove_punctuation(line)
    word_list = line_no_punct.split(" ")
    word_list = [word for word in word_list if len(word) > 0]
    word_list.sort(key=lambda word: (len(word), str(word)))
    
    return " ".join(word_list)

with open(abe_file) as abe_in, open(abe_rearranged, "w") as abe_out:
    for line in abe_in:
        rearranged_line = rearrange_line(line[:-1])
        abe_out.write(rearranged_line + '\n')
        
with open('smedleybutler.txt') as sb:
    smed_set = { a_line for a_line in sb
                  for a_word in a_line.split(" ") if len(a_word) > 9}

with open('bigwords.txt', 'w') as bw:
    bw.writelines( smed_set  )

with open('bigwords.txt', 'r') as bw:
    content = bw.read()
    print(content)
    
    
# os.system( 'type bigwords.txt' )
        
with open('abespeech.txt') as abe:
    for line_idx, a_line in enumerate( abe, 1 ):
        rev_line = list( a_line[: -1] )
        rev_line.reverse()
        print(f'{line_idx}\t {"".join(rev_line)}')
