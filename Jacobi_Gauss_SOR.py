import numpy as np

def getAllMatrices(matrixA):
    n = len(matrixA)
    
    diagonalMatrix = np.zeros((n, n))
    lowerMatrix = np.zeros((n, n))
    upperMatrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                diagonalMatrix[i][j] = matrixA[i][j]
            elif i > j:
                lowerMatrix[i][j] = matrixA[i][j]
            else:
                upperMatrix[i][j] = matrixA[i][j]
    
    return diagonalMatrix, lowerMatrix, upperMatrix

def solveUsingJacobi(matrixA, b, initialValue, tolerance, max_iterations):
    diagonalMatrix, lowerMatrix, upperMatrix = getAllMatrices(matrixA)
    n = len(matrixA)
    x = np.array(initialValue)
    iteration = 1

    while iteration < max_iterations:
        x_new = np.linalg.solve(diagonalMatrix, b - np.dot(lowerMatrix + upperMatrix, x))
        error = np.linalg.norm(x_new - x)
        if error <= tolerance:
            print(f"Matrix converged after {iteration} iterations and the error is {round(error,4) }")
            return x_new
        x = x_new
        iteration += 1

    print(f"Maximum iterations of ({max_iterations}) reached and error is {round(error,4)}")
    return x

def solveUsingGaussSeidel(matrixA, b, initialValue, tolerance, max_iterations):
    diagonalMatrix, lowerMatrix, upperMatrix = getAllMatrices(matrixA)
    n = len(matrixA)
    x = np.array(initialValue)
    iteration = 1

    while iteration < max_iterations:
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = (1 / diagonalMatrix[i][i]) * (b[i] - np.dot(upperMatrix[i], x) - np.dot(lowerMatrix[i], x_new))
        
        error = np.linalg.norm(x_new - x)
        if error <= tolerance:
            print(f"Matrix converged after {iteration} iterations and the error is {round(error,4) }")
            return x_new
        x = x_new
        iteration += 1

    print(f"Maximum iterations of ({max_iterations}) reached and error is {round(error,4)}")
    return x


def solveUsingSOR(matrixA, b, initialValue, omega, tolerance, max_iterations):
    diagonalMatrix, lowerMatrix, upperMatrix = getAllMatrices(matrixA)
    n = len(matrixA)
    x = np.array(initialValue)
    iteration = 1

    while iteration < max_iterations:
        x_new = np.zeros(n)
        for i in range(n):
            temporaryValue1 = (1 - omega) * diagonalMatrix[i][i] * x[i]
            temporaryValue2 = omega * (b[i] - np.dot(upperMatrix[i], x))
            temporaryValue3 = omega * np.dot(lowerMatrix[i], x_new)
            x_new[i] = (1 / (omega * diagonalMatrix[i][i] + (1 - omega) * diagonalMatrix[i][i])) * (temporaryValue1 + temporaryValue2 - temporaryValue3)

        error = np.linalg.norm(x_new - x)
        if error <= tolerance:
            print(f"Matrix converged after {iteration} iterations and the error is {round(error,4) }")
            return x_new
        x = x_new
        iteration += 1

    print(f"Maximum iterations of ({max_iterations}) reached and error is {round(error,4)}")
    return x

# Example usage:
matrixA = [
    [3, -1, 0, 0, 0, 1/2],
    [-1, 3, -1, 0, 1/2, 0],
    [0, -1, 3, -1, 0, 0],
    [0, 0, -1, 3, -1, 0],
    [0, 1/2, 0, -1, 3, -1],
    [1/2, 0, 0, 0, -1, 3]
]

b = [5/2, 3/2, 1, 1, 3/2, 5/2]
initialValue = [0, 0, 0, 0, 0, 0]
iteration = 100
tolerance=0.01

solJacobi = solveUsingJacobi(matrixA, b, initialValue, tolerance, iteration)
print("Solution using Jacobi method:", np.round(solJacobi, 4))

solGauss = solveUsingGaussSeidel(matrixA, b, initialValue, tolerance, iteration)
print("Solution using Gauss-Seidel method:", np.round(solGauss, 4))

omega = 1.1  # You can adjust the value of omega as needed

solSOR = solveUsingSOR(matrixA, b, initialValue, omega, tolerance, iteration)
print("Solution using SOR method:", np.round(solSOR, 4))

