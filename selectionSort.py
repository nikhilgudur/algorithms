print("Enter an array to be sorted")
arr = list(map(int, input().split()))

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        arr[small], arr[i] = arr[i], arr[small]

    return arr

print(*selectionSort(arr))