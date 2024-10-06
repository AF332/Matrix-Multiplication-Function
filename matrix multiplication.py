def matrix_multiplication(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in Matrix A must be equal to the number of rows in Matrix B")
    
    # Initialise the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for in_ in range(len(A))] # Creates a matrix of zeros with the size of the result matrix.

    # Perform matrix multiplication
    for i in range(len(A)): # Loop through rows A
        for j in range(len(B[0])): # Loops thorugh columns of B
            for k in range(len(B)): # Loops though rows of B (and columns of A)
                result[i][j] += A[i][k] * B[k][j] # performs the multiplication and accumulation of values in the result matrix.

    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

try:
    result = matrix_multiplication(A, B)
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)