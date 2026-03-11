# Question 5

### Implementation and Results

Solution coded in [merge_ll.py](https://github.com/ePinonIV/cs361l-homework-2/blob/main/question5/merge_ll.py), here is the output from running the code using the given example lists:

```
$ python3 merge_ll.py
--------------------
list1:
1 -> 2 -> 4
list2:
1 -> 3 -> 4
Lists merged, printing result...
1 -> 1 -> 2 -> 3 -> 4 -> 4
--------------------
```

### Explanation

This code simply compares the values of the heads of the two given lists and adds the lower one as the next value of the new merged list. Then it increments the list it took the value from and compares until it reaches the end of one of the lists. Then, it just adds the rest of whatever list wasn't empty, as the list was already sorted, it will nicely complete the merged list.