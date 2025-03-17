# Linear Functions and Matrix Operations

## Overview
This project implements various mathematical operations using Python, NumPy, and Matplotlib. The functionalities include:

- Computing and plotting a linear function.
- Determining the slope and intercept of a line given two points.
- Performing matrix operations such as transpose, determinant, and inverse.
- Multiplying two 3×3 matrices.

This project serves as both a mathematical exploration and a practical application of key computational concepts, helping reinforce my understanding of linear functions and matrix operations while integrating them into Python programming.

---

## Terminologies and Their Usage

### **1. Linear Function**
A **linear function** is a mathematical equation of the form:

\[ f(x) = mx + b \]

- **m (Slope)**: Represents the rate of change of the function. If `m` is positive, the function increases; if negative, it decreases.
- **b (Intercept)**: The point where the line crosses the y-axis (when `x = 0`).
- **x-values**: The independent variable values.
- **y-values**: The dependent variable values computed using `f(x) = mx + b`.

#### **Use Case in This Project**
This project computes `y-values` for a range of `x-values` and plots them using Matplotlib to visualize the linear function. This is useful in trend analysis, finance, and physics.

---

### **2. NumPy**
**NumPy (Numerical Python)** is a powerful library for handling arrays and performing numerical operations efficiently.

#### **Why NumPy?**
- Handles large datasets faster than Python lists.
- Provides built-in functions for matrix operations.
- Supports **vectorized computations**, avoiding slow Python loops.

#### **Key NumPy Functions Used**
- `np.linspace(start, stop, num)`: Generates evenly spaced values.
- `np.array()`: Creates arrays for mathematical operations.
- `np.linalg.det()`: Computes the determinant of a matrix.
- `np.linalg.inv()`: Computes the inverse of a matrix.
- `np.dot()`: Performs matrix multiplication.

---

### **3. Matplotlib**
**Matplotlib** is a plotting library that visualizes data in Python.

#### **Why Matplotlib?**
- Allows easy visualization of mathematical functions.
- Supports multiple graph types like line, scatter, bar, etc.
- Enables customization with labels, legends, and grid options.

#### **Key Matplotlib Functions Used**
- `plt.plot(x_values, y_values)`: Plots the linear function.
- `plt.xlabel()`, `plt.ylabel()`: Labels axes.
- `plt.grid()`: Adds grid lines for better readability.
- `plt.show()`: Displays the plot.

---

### **4. Matrix Operations**
A **matrix** is a rectangular array of numbers arranged in rows and columns. Matrices are widely used in engineering, physics, computer science, and machine learning.

#### **Operations Performed in This Project**
- **Transpose** (`matrix.T`): Flips the rows and columns.
- **Determinant** (`np.linalg.det(matrix)`): Computes a scalar value that determines if a matrix is invertible.
- **Inverse** (`np.linalg.inv(matrix)`): Computes the matrix that, when multiplied with the original matrix, results in the identity matrix. If determinant is `0`, the matrix is **singular** and cannot be inverted.
- **Matrix Multiplication** (`np.dot(matrix1, matrix2)`): Computes the product of two matrices.

---

## Prerequisites
Ensure you have Python 3 installed on your system. This project requires the following dependencies:

- **NumPy**: For numerical operations.
- **Matplotlib**: For plotting graphs.

### Installing Dependencies
If you haven’t already, install the required packages inside a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate  # Activate the virtual environment
pip install numpy matplotlib
```

---

## Usage

### 1. Clone the Repository (if applicable)
If you are using Git, you can clone this repository:

```bash
git clone <repository_url>
cd <repository_folder>
```
Otherwise, ensure you have the `linear_matrix.py` file saved in your working directory.

### 2. Running the Script
After navigating to the project directory, activate the virtual environment (if not already active):

```bash
source myenv/bin/activate  # Mac/Linux
myenv\Scripts\activate    # Windows (Command Prompt)
```

Now, run the script:

```bash
python linear_matrix.py
```

---

## Functionality Details

### 1. Plotting a Linear Function
Computes and plots the function:

\[ f(x) = mx + b \]

- **`m`**: Slope of the line.
- **`b`**: Y-intercept.
- **`x_values`**: Range of x-values (generated using `linspace` if not provided).

#### Example:
```python
linear_equation(2, 5)
```

---

### 2. Computing Slope and Intercept
Calculates:

\[ m = \frac{y_2 - y_1}{x_2 - x_1} \]
\[ b = y_1 - m \times x_1 \]

---

### 3. Matrix Operations
Performs:
- **Transpose**
- **Determinant**
- **Inverse (if possible)**

---

### 4. Matrix Multiplication
Multiplies two **random 3×3 matrices** using `np.dot()`.

---

## Error Handling
- If the determinant is `0`, the script alerts the user instead of attempting an inverse calculation.
- If an incorrect file path is used when running the script, Python returns a **FileNotFoundError**.

---

## Troubleshooting
**Issue: "pip: command not found"**
- Ensure Python is installed.
- Run `python3 -m ensurepip`.

**Issue: "ModuleNotFoundError: No module named 'numpy'"**
- Ensure dependencies are installed inside your virtual environment.
- Activate the environment using `source myenv/bin/activate`.

---

## License
This project is open-source and available for personal and educational use.

---

## Author
Developed by **Sahabia Yakubu**

For inquiries, reach out at:
**Sahabia Yakubu**  
📧 **Email**: yakubukarim12@gmail.com  
🐙 **GitHub**: [sahadevgh](https://github.com/sahadevgh)  
🐦 **Twitter/X**: @sahadevgh

---

Happy Coding! 
