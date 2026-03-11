import time
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# classic insertion sort like we've seen in class
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# don't need to pass n and m since can get lengths from left/right
def merge_sort(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # need extend to add multiple items at once
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# combine insertion and merge with threshold
def hybrid_sort(arr, k):
    # switch to insertion sort if size <= k
    if len(arr) <= k:
        return insertion_sort(arr)
    
    # otherwise run merge sort
    mid = len(arr) // 2 # take floor
    left = hybrid_sort(arr[:mid], k)
    right = hybrid_sort(arr[mid:], k)
    
    return merge_sort(left, right)

def main():
    # 1. create array sizes and k values
    array_sizes = [500, 2000, 10000]
    k_values = [1, 2, 4, 8, 16, 32, 64]
    iterations = 5

    # make results list that holds space for each array size
    results = {size: [] for size in array_sizes}

    # 2. loop through each array size
    for n in array_sizes:
        print("Testing array size: " + str(n) + "...")
        # 3. loop through each k value and repeat sort 5 times
        for k in k_values:
            # record time
            total_time = 0
            for i in range(iterations):
                # generate random array each time
                data = [random.randint(0, 100000) for i in range(n)]

                start_time = time.perf_counter()
                hybrid_sort(data, k)
                end_time = time.perf_counter()

                # note time and convert to ms
                total_time += (end_time - start_time) * 1000

            avg_time = total_time / iterations
            results[n].append(avg_time)

    # 4. plotting results
    plt.figure(figsize=(10, 6))
    
    for n in array_sizes:
        plt.plot(k_values, results[n], marker='.', label=f'n={n}')

    plt.title("Hybrid Sort Performance: Threshold k vs. Runtime")
    plt.xlabel('Threshold $k{}$')
    plt.ylabel('Average Runtime (ms)')
    plt.legend()
    plt.grid(True)
    plt.savefig("runtime_plot.png")
    plt.show
            
    
if __name__ == "__main__":
    main()