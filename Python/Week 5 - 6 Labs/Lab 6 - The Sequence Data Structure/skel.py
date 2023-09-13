#!/usr/bin/env python3
import random           # To generate random integers

# Find common elements for a pair of iterators
def find_common_unique_elements( iter1, iter2 ):
    list_with_common = []
    for iter1_elem in iter1:
        if iter1_elem in iter2 and iter1_elem not in list_with_common:
            list_with_common.append( iter1_elem )

    return list_with_common

def find_common_elems_buncha_iters( buncha_iters ):
    
    common_elems = find_common_unique_elements( buncha_iters[0], buncha_iters[1] )

    for an_iter in buncha_iters[ 2: ]:
        common_elems = find_common_unique_elements( common_elems, an_iter )

   
    return common_elems

def gen_return_random_num_list( num_items ) :
    return [ random.randint(0, 20) for _ in range(0, num_items)]

def main( ):
    num_iterators = int( input( "Enter number of iterators (5 - 10) "))
    num_each_iterator = int( input("Enter number for each iterator (15 - 20) "))
   
    buncha_iters = [ gen_return_random_num_list (num_each_iterator) 
                    for _ in range(0, num_iterators)]

    for iterative in buncha_iters:
        print(f"{sorted(iterative)}")

    print(f'Elements common to all lists: {find_common_elems_buncha_iters( buncha_iters )}')

main()
