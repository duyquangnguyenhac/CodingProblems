import random
def quicksort(arr):
    def pivot(low, high):
        p = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < p:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]            
        return i

    def recur(low, high):
        if low < high:
            pivot_idx = pivot(low, high)
            recur(low, pivot_idx - 1)
            recur(pivot_idx + 1, high)
    recur(0, len(arr) - 1)
    return arr

print(quicksort([1,3,1,2,8]))
