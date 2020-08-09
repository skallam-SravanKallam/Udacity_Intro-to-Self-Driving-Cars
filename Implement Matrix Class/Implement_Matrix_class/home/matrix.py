import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 2:
            det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0] #ad-bc for a 2*2 matrix
            
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace_val = 0
        for i in range(self.h):
            trace_val += self.g[i][i] 
        
        return trace_val
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        if self.h == 1:
            if self.g[0][0] == 0: # check you dont get a 1 over 0 error
                raise(Error,"matrix cannot be inverted")
            else:
                inv = ([[1/self.g[0][0]]]) 
                return Matrix(inv)
        
        
        elif self.h ==2:
            
            if self.determinant() == 0: # check you dont get a 1 over 0 error
                raise(Error,"matrix cannot be inverted")

            else:
                det = self.determinant()
                a = (1/det) * self.g[0][0]
                b = (1/det) * self.g[0][1]
                c = (1/det) * self.g[1][0]
                d = (1/det) * self.g[1][1]
                inv = [[d,-b],[-c,a]]
                return Matrix(inv)
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        Tr = []
        for i in range(self.w):
            new_row = []
            for j in range(self.h):
                new_row.append(self.g[j][i])
            Tr.append(new_row)
        return Matrix(Tr)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:
            add= zeroes(self.h,self.w)
            for i in range(self.h):
                for j in range(self.w):
                    add[i][j] = self.g[i][j]+other.g[i][j]
            return add

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        neg= zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                neg[i][j] = -1*self.g[i][j]
              
        return neg
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:
            sub = zeroes(self.h,self.w)
            for i in range(self.h):
                for j in range(self.w):
                    sub[i][j] = self.g[i][j] - other.g[i][j]
            return sub        
        
        #   
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h: 
            raise(ValueError, "Matrices can only be multiplied if columns of first is equal to the number of rows in second") 
        #   
        # TODO - your code here
        #
        mul = zeroes(self.h,other.w)
        for i in range(self.h):
            for j in range(other.w):
                val = 0
                for k in range(self.w):
                    val += self.g[i][k]*other.g[k][j]
                mul[i][j] = val    
            
        return mul
        
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        rmul = []
        for i in range(self.h):
            new_row= []
            for j in range(self.w):
                new_row.append(other*self.g[i][j])
            rmul.append(new_row)    
        return Matrix(rmul) #converting to a matrix
        
        
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            #skallam - did not understand what to implement here..