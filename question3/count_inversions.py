# Modify merge sort algorithm to count inversions

# based on merge sort from hybrid_sort in Q2
# will return two things:
#   - array it sorted 
#   - the number of inversions it counted
def count_inversions(arr):
    # base case: single element has 0 inversions
    if len(arr) <= 1:
        return arr, 0

    # split array
    mid = len(arr) // 2 # take floor
    # get inversions from each half as well
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])

    # merge and count inversions
    result = []
    i = j = 0
    current_inv = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # if right[j] smaller, it is inverted with every element in left
            current_inv += (len(left) - i) # don't want to count iteration itself

    # need extend to add multiple items at once
    result.extend(left[i:])
    result.extend(right[j:])

    #return merged array and all inversions counted
    all_inv = left_inv + current_inv + right_inv
    return result, all_inv


def main():
    print("--------------------")

    # make example arrays
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 3, 2, 1]
    arr3 = [2, 4, 1, 3]

    # run merge sort to count
    print("arr1: " + str(arr1))
    sorted_arr1, arr1_inv = count_inversions(arr1)
    print("Number of inversions in arr1 = " + str(arr1_inv))
    print("sorted arr1: " + str(arr1) + "\n")

    print("arr2: " + str(arr2))
    sorted_arr2, arr2_inv = count_inversions(arr2)
    print("Number of inversions in arr2 = " + str(arr2_inv))
    print("sorted arr2: " + str(sorted_arr2) + "\n")

    print("arr3: " + str(arr3))
    sorted_arr3, arr3_inv = count_inversions(arr3)
    print("Number of inversions in arr3 = " + str(arr3_inv))
    print("sorted arr3: " + str(arr3))


    print("--------------------")
    
if __name__ == "__main__":
    main()