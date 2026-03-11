# Question 1

### Implementation and Results

I implemented the Towers of Hanoi problem recursively in the file towers_recursive.py. Here is the output of running the code with $n = 3$:

```
$ python3 towers_recursive.py 
----------- Initial state:
A: [3, 2, 1]
B: []
C: []
------------------- MOVE 1
Move disk 1 from tower A to tower B
A: [3, 2]
B: [1]
C: []
------------------- MOVE 2
Move disk 2 from tower A to tower C
A: [3]
B: [2]
C: [1]
------------------- MOVE 3
Move disk 1 from tower B to tower C
A: []
B: [2, 1]
C: [3]
------------------- MOVE 4
Move disk 3 from tower A to tower B
A: []
B: [3]
C: [2, 1]
------------------- MOVE 5
Move disk 1 from tower C to tower A
A: [2]
B: [1]
C: [3]
------------------- MOVE 6
Move disk 2 from tower C to tower B
A: []
B: [3, 2]
C: [1]
------------------- MOVE 7
Move disk 1 from tower A to tower B
A: []
B: [3, 2, 1]
C: []
------------------- MOVE 8
----------- Complete
```

Here is the output of the code running with $n = 5$:

```
$ python3 towers_recursive.py 
----------- Initial state:
A: [5, 4, 3, 2, 1]
B: []
C: []
------------------- MOVE 1
Move disk 1 from tower A to tower B
A: [5, 4, 3, 2]
B: [1]
C: []
------------------- MOVE 2
Move disk 2 from tower A to tower C
A: [5, 4, 3]
B: [2]
C: [1]
------------------- MOVE 3
Move disk 1 from tower B to tower C
A: []
B: [2, 1]
C: [5, 4, 3]
------------------- MOVE 4
Move disk 3 from tower A to tower B
A: [5, 4]
B: [3]
C: [2, 1]
------------------- MOVE 5
Move disk 1 from tower C to tower A
A: [2]
B: [5, 4, 1]
C: [3]
------------------- MOVE 6
Move disk 2 from tower C to tower B
A: []
B: [3, 2]
C: [5, 4, 1]
------------------- MOVE 7
Move disk 1 from tower A to tower B
A: [5, 4]
B: [3, 2, 1]
C: []
------------------- MOVE 8
Move disk 4 from tower A to tower C
A: [5]
B: [4]
C: [3, 2, 1]
------------------- MOVE 9
Move disk 1 from tower B to tower C
A: [3, 2]
B: [4, 1]
C: [5]
------------------- MOVE 10
Move disk 2 from tower B to tower A
A: [3]
B: [5, 2]
C: [4, 1]
------------------- MOVE 11
Move disk 1 from tower C to tower A
A: [4]
B: [5, 2, 1]
C: [3]
------------------- MOVE 12
Move disk 3 from tower B to tower C
A: []
B: [4, 3]
C: [5, 2, 1]
------------------- MOVE 13
Move disk 1 from tower A to tower B
A: [5, 2]
B: [1]
C: [4, 3]
------------------- MOVE 14
Move disk 2 from tower A to tower C
A: [5]
B: [4, 3, 2]
C: [1]
------------------- MOVE 15
Move disk 1 from tower B to tower C
A: []
B: [4, 3, 2, 1]
C: [5]
------------------- MOVE 16
Move disk 5 from tower A to tower B
A: []
B: [5]
C: [4, 3, 2, 1]
------------------- MOVE 17
Move disk 1 from tower C to tower A
A: [4, 3, 2]
B: [1]
C: [5]
------------------- MOVE 18
Move disk 2 from tower C to tower B
A: [4, 3]
B: [5, 2]
C: [1]
------------------- MOVE 19
Move disk 1 from tower A to tower B
A: []
B: [5, 2, 1]
C: [4, 3]
------------------- MOVE 20
Move disk 3 from tower C to tower A
A: [4]
B: [3]
C: [5, 2, 1]
------------------- MOVE 21
Move disk 1 from tower B to tower C
A: [5, 2]
B: [4, 1]
C: [3]
------------------- MOVE 22
Move disk 2 from tower B to tower A
A: [5]
B: [3, 2]
C: [4, 1]
------------------- MOVE 23
Move disk 1 from tower C to tower A
A: [4]
B: [3, 2, 1]
C: [5]
------------------- MOVE 24
Move disk 4 from tower C to tower B
A: []
B: [5, 4]
C: [3, 2, 1]
------------------- MOVE 25
Move disk 1 from tower A to tower B
A: [3, 2]
B: [5, 4, 1]
C: []
------------------- MOVE 26
Move disk 2 from tower A to tower C
A: [3]
B: [2]
C: [5, 4, 1]
------------------- MOVE 27
Move disk 1 from tower B to tower C
A: [5, 4]
B: [2, 1]
C: [3]
------------------- MOVE 28
Move disk 3 from tower A to tower B
A: []
B: [5, 4, 3]
C: [2, 1]
------------------- MOVE 29
Move disk 1 from tower C to tower A
A: [2]
B: [1]
C: [5, 4, 3]
------------------- MOVE 30
Move disk 2 from tower C to tower B
A: []
B: [5, 4, 3, 2]
C: [1]
------------------- MOVE 31
Move disk 1 from tower A to tower B
A: []
B: [5, 4, 3, 2, 1]
C: []
------------------- MOVE 32
----------- Complete
```

### Time Complexity Analysis

Let $T(n)$ represent the number of moves needed to sort the towers for $n$ disks.

At the first recursive call, we move $n-1$ disks, so it takes $T(n-1)$ time.

The largest disks is moved from one tower to another with constant, or $O(1)$ time.

Then there is a second recursive call with $T(n-1)$ time.

The full recurrence relation is: $T(n) = 2T(n-1) + 1$

Analyzing this with substitution:

$T(n) = 2T(n-1) + 1$

$T(n) = 2T(n-2) + 1 = 2[2T(n-1) + 1] + 1 = 4T(n-1) + 3$

$T(n) = 2T(n-3) + 1 = 2[4T(n-1) + 3] + 1 = 8T(n-1) + 7$

...

$T(1) = 2^n T(0) + O(1)$

Following this for $k$ steps to the base case of $k = n-1$ we get that the driving term is constant so has $O(1) complexity and we can look to the homogeneous term for the time complexity

$T(n) = 2^k T(n-k) + (2^k - 1)$

Thus, by susbsitution, the time complexity of the algorithm is $O(2^n)$.