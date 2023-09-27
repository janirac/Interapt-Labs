# Poor man's implementation of a 2-D matrix class
import operator

class Matrix:
    '''
        data is a list. order is a tuple of (rows, columns)
        Maybe explore additional arg checking?
    '''
    def __init__( self, data, order ):
        # Should we check if 'order' is a tuple of two INTEGERS???
        if not all ([isinstance(elem, int) for elem in order]) or len(order) != 2:
            raise ValueError ("Dimensions passed to CTOR are not integral or two elements not passed for dimensions")

        # Check if order arg matches data dimensions
        self._rows = order[0]
        self._columns = order[1]
        if len_data := len(data) != self._rows * self._columns:
            raise ValueError (f'data passed has {len_data} elements; does not match'
                              f'dimensions ({self._rows} X {self._columns}')  
        # Check if ALL entries are numeric
        if any([type(elem) not in (int, float) for elem in data]):
            raise TypeError('Not all values in data passed to CTOR are numeric')
        
        # OK that's enough - let's load the matrix
        self._data = data.copy()
                
    # Let's print it out
    def __str__(self):
        mat_str = ""
        for row in range(self._rows):
            start_idx = row * self._columns
            end_idx = (row + 1) * self._columns
            mat_str += "| " + " ".join([str(self._data[elem]) for elem in range(start_idx, end_idx)]) + " |\n"
            
        return mat_str
    
    def _operate_on_matrices(self, rho_mat, operation):
        # Check if rows and columns of both match
        if self._rows != rho_mat._rows or self._columns != rho_mat._columns:
            raise ValueError ('Matrix dimensions incompatible')
        # All good...let's add elements, return result
        return Matrix([operation(elem1, elem2) for (elem1, elem2) in zip(self._data, rho_mat._data)], 
                             (self._rows, self._columns))
        
    
    # Add two matrices
    def __add__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.add)
    
    # Subtract two matrices
    def __sub__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.sub)  
    
    # Multiply (dot product, actually) two matrices
    def __mul__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.mul)      
    
    # Divide (element divide) two matrices
    def __truediv__(self, rho_mat):       
        return self._operate_on_matrices(rho_mat, operator.truediv)     
        
        
        
if __name__ == "__main__":
    mat = Matrix([1,2,3,4,5,6], (3, 2))
    mat2 = Matrix([11,12,13,14,15,16], (3, 2))
    
    print("Matrix 'mat':")
    print(mat)
    print("Matrix 'mat2':")
    print(mat2)    
    # Add them, print result 
    sum_mats = mat + mat2  
    print("Sum of the above matrices:")
    print(sum_mats)  
    diff_mats = sum_mats - mat
    print("Difference of the above matrices:")
    print(diff_mats)  
    dot_prod_mats = sum_mats * mat
    print("Dot product of the above matrices:")
    print(dot_prod_mats)     
         

