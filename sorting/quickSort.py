print("Enter an array to be sorted quickly")
arr = list(map(int, input().split()))
n = len(arr)-1

def partition(arr, lo, hi):
    pivot = arr[hi]
    pointer = lo

    for i in range(lo, hi):
        if arr[i] < pivot:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    arr[pointer], arr[hi] = arr[hi], arr[pointer]
    
    return pointer

def quickSort(arr, lo, hi):
    if lo < hi:
        pointer = partition(arr, lo, hi)

        quickSort(arr, lo, pointer-1)
        quickSort(arr, pointer+1, hi)

    return arr

quickSort(arr, 0, n)
print("Sorted array")
print(*arr)