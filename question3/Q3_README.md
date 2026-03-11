# Question 3

### Implementation and Results

Code made in count_inversions.py, check file for to see my implementation. Here is the output of running the code, using the examples to ensure it works:

```
$ python3 count_inversions.py
--------------------
arr1: [1, 2, 3, 4]
Number of inversions in arr1 = 0
sorted arr1: [1, 2, 3, 4]

arr2: [4, 3, 2, 1]
Number of inversions in arr2 = 6
sorted arr2: [1, 2, 3, 4]

arr3: [2, 4, 1, 3]
Number of inversions in arr3 = 3
sorted arr3: [2, 4, 1, 3]
--------------------
```

### Questions:

1. What's the maximum number of inversions possible for an array of size $n$?

The maximum number of inversions possible for an array of size $n$ would arise if the array is perfectly sorted in reverse.
In this case, the first element will have inversions with every element after it, so $n-1$ inversions.
The second element will have inversions with every element after it, so $n-2$ inversions.
This will continue until the second to last element, which will have 1 inversion.
Then the last element will have 0 inversions, since there are no more elements after it.

Adding up the inversions, we get: $(n-1) + (n-2) + ... + 1 + 0$

Which is simply the arithmetic series that is equal to $n(n-1) /2$

So the max number of inversions for an array of size $n$ is $n(n-1) / 2$

Which we can verify by using the example array that is perfectly reverse sorted; it has 4 elements, so $n=4$ → $4(4-1) / 2 = 4(3) / 2 = 12 / 2 = 6$.

2. How does the inversion count relate to sorting algorithms like bubble sort?

The inversion count relates to sorting algorithms like bubble sort because the number of inversions would be the number of swaps that bubble sort would need to do.
This is because of how bubble sort works - when it swaps two elements that are next to each other, it is essentially fixing one inversion.
This also shows how for very poorly initially sorted arrays, sorting algorithms like bubble sort will perform very poorly, since they will have many inversions to fix.