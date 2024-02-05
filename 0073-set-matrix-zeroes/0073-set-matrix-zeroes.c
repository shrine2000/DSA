void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int isRowZero = 0, isColZero = 0;

    for (int j = 0; j < *matrixColSize; ++j) {
        if (matrix[0][j] == 0) {
            isRowZero = 1;
            break;
        }
    }

    for (int i = 0; i < matrixSize; ++i) {
        if (matrix[i][0] == 0) {
            isColZero = 1;
            break;
        }
    }

    for (int i = 1; i < matrixSize; ++i) {
        for (int j = 1; j < *matrixColSize; ++j) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    for (int i = 1; i < matrixSize; ++i) {
        for (int j = 1; j < *matrixColSize; ++j) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (isRowZero) {
        for (int j = 0; j < *matrixColSize; ++j) {
            matrix[0][j] = 0;
        }
    }

    if (isColZero) {
        for (int i = 0; i < matrixSize; ++i) {
            matrix[i][0] = 0;
        }
    }
}
