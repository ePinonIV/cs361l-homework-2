# Question 6

### Implementation and Results

Solution coded in [diagonal_matrix_sort.py](https://github.com/ePinonIV/cs361l-homework-2/blob/main/question6/diagonal_matrix_sort.py), here is the output from running the code using the given example matrix:

```
$ python3 diagonal_matrix_sort.py
-------------------
original example matrix:
[3, 3, 1, 1]
[2, 2, 1, 2]
[1, 1, 1, 2]

sorted diagonal example matrix:
[1, 1, 1, 1]
[1, 2, 2, 2]
[1, 2, 3, 3]

-------------------

test matrix 1:
[5, 6, 3, 1]
[3, 2, 3, 4]
[1, 4, 2, 5]

sorted test matrix 1:
[2, 3, 3, 1]
[3, 2, 5, 4]
[1, 4, 5, 6]

-------------------
```

### Explanation

To implement this problem I could see how it was going to be difficult with basic arrays so I looked into different data structures that already exists in python and found the [collections](https://docs.python.org/3/library/collections.html#collections.defaultdict) library.
I decided to use the [defaultdict](https://www.geeksforgeeks.org/python/defaultdict-in-python/) structure as it seemed useful for being able to store keys and make a new list when getting a new key (which is good when I don't know the exact range of the values that are going to be in the matrix I need to sort).

The code works by looping through the matrix and adding each value to the default dictionary to store them grouped by their values. Then it loops through the keys and sorts them with the python sort function. Finally, it pops them back into the matrix in reverse order so that the diagonals have the largest values in the bottom right.