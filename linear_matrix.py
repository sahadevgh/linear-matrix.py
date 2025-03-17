import numpy as np
import matplotlib.pyplot as plt

# Part A
# Functiong to compute y-values for the linear equation and 
# Plotting the linear function
def linear_equation(m, b, x_values=None):
    if x_values is None:
        x_values = np.linspace(-10, 10, 100)  # Using linspace to generate 100 values between -10 and 10
    y_values = m * x_values + b
    
    # Plot
    plt.plot(x_values, y_values, label=f"y = {m}x + {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Function Plot")
    plt.legend()
    plt.grid()
    plt.show()
    
    return y_values

# Part B
# Computing slope and intercept
def compute_slope_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

# Part C 
# Matrix operations
def matrix_operations():
    # Generate a random 3x3 matrix
    matrix = np.random.randint(1, 10, (3, 3))
    print("Original Matrix:\n", matrix)
    
    # Transpose
    transpose = matrix.T
    print("\nTranspose:\n", transpose)
    
    # Determinant
    determinant = np.linalg.det(matrix)
    print("\nDeterminant:", determinant)
    
    # Inverse
    if np.abs(determinant) > 1e-6:  # Check if determinant is not zero
        inverse = np.linalg.inv(matrix)
        print("\nInverse:\n", inverse)
    else:
        print("\nMatrix is singular (no inverse).")

# Part D
# Multiplying two 3x3 matrices
def matrix_multiplication():
    matrix1 = np.random.randint(1, 10, (3, 3))
    matrix2 = np.random.randint(1, 10, (3, 3))
    
    print("Matrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)
    
    product = np.dot(matrix1, matrix2)
    print("\nMatrix Multiplication Result:\n", product)

# Testing the functions
if __name__ == "__main__":
    # Test Part A
    linear_equation(2, 5)
    
    # Test Part B
    m, b = compute_slope_intercept(1, 3, 4, 11)
    print(f"\nSlope: {m}, Intercept: {b}")
    
    # Test Part C
    matrix_operations()
    
    # Test Part D
    matrix_multiplication()
