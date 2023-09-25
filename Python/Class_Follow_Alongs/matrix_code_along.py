''' Poor man's implementation of a 2-D matrix class
    Pass a list of numbers and a TUPLE of #rows/#cols to CTOR
    Matrix object has 3 properties:
    
    _rows = number of rows
    _ columns = number of columns
    _data = elements of the matrix
    
    my_mat = Matrix( [1,2,3,4,5,6], (2,3) ) yields a 2 X 3 matrix
    printable representation:
    
    | 1 2 |
    | 3 4 |
    | 5 6 |
 
    Let's forgo creating properties for now (if we have time, maybe)     
'''

class Matrix:
    def __init__(self, data, order):
        if len(order) != 2 or type(order[0] != int or type(order[1]) != int):
            raise ValueError(f'Elements in {order} not numeric or wrong # of elements passed in')
        
        if order[0] * order[1] != len(data):
            raise ValueError(f'Dimension mismatch between {order} and {data}')
        
        if any([type(elem) not in (int, float) for elem in data]):
            raise ValueError(f'Not all entires in {order} are numeric')
        
    '''
        data is a list. order is a tuple of (rows, columns)
        Maybe explore some arg checking?
    '''
    # Code the CTOR here
    
        # Should we check if 'order' is a tuple of two INTEGERS???
        
        # Check if order arg matches data dimensions. If not, raise exception
        # Remember that order is a TUPLE
 
        # Check if ALL entries are numeric. If not, raise exception

        
        # OK that's enough - let's load the matrix by copying data arg into instance variable
                
    # Let's print it out. Use the dunder overload
 
        # Initialize an empty string and concatenate data and row delimiters
        #
        # Let's think about what we want this string to look like when done
        # Note each line is enclosed in |   |
        # We need a way of indexing the elements in the _data instance by
        # calculating something using the _rows and _columns instance variables
        #
        # The printed result will have _rows printed, so we could use some sort of loop?
        #
        # Inside that loop, we want to concatenate elements from _data based on
        # a calculation using rows/columns
        # Maybe some examples will help?
        #
        # for a 2 X 3 matrix, we want these indexes from _data:
        # 0  1      Each loop iteration produces a row with these index elements from _data
        # 2  3
        # 4  5
        #
        # For a 4 X 3
        #
        # 0 1 2 3
        # 4 5 6 7
        # 8 9 10 11
        #
        # Surround each row with a "|" 
    
    # Add two matrices - let's look up the dunder used to overload '+'
     
        # Check if rows and columns of both match
        
        # All good...let's add elements, return result
        # Any thoughts on how to generate a structure that allows us to easily add
        # the numbers in the Matrix objects?

        
if __name__ == "__main__":
    mat = Matrix([1,2,3,4,5,6], (3, 2))
    mat2 = Matrix([11,12,13,14,15,16], (3, 2))
    
    print("Matrix 'mat':")
    print(mat)
    '''       
    | 1 2 |
    | 3 4 |
    | 5 6 |
    '''
    print("Matrix 'mat2':")
    print(mat2)    
    '''       
    | 11 12 |
    | 13 14 |
    | 15 16 |
    '''    
    # Add them, print result 
    sum_mats = mat + mat2
    
    print("Sum of the above matrices:")
    print(sum_mats) 