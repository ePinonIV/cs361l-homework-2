from collections import defaultdict
import math # not needed?

def sort_matrix_diagonals(mat):
    """
    Sorts each diagonal of an m x n matrix in ascending order.
    """
    if not mat or not mat[0]:
        return mat
        
    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)
    
    # group by i-j formula
    for i in range(m):
        for j in range(n):
            diagonals[i - j].append(mat[i][j])
            
    # sort descending for O(1) popping from the end
    for key in diagonals:
        diagonals[key].sort(reverse=True)
        
    # replace by popping back into matrix
    for i in range(m):
        for j in range(n):
            mat[i][j] = diagonals[i - j].pop()
            
    return mat

def main():
    # example input
    input_mat = [
        [3, 3, 1, 1],
        [2, 2, 1, 2],
        [1, 1, 1, 2]
    ]

    print("Original Matrix:")
    for row in input_mat:
        print(row)

    sorted_mat = sort_matrix_diagonals(input_mat)

    print("\nSorted Diagonal Matrix:")
    for row in sorted_mat:
        print(row)

if __name__ == "__main__":
    main()
