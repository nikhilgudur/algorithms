print("Enter array to be sorted")
arr = list(map(int, input().split()))

def merge(left, right):

    arr = list()
    l = 0
    r = 0

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1
    while l < len(left):

        if l < len(left):
            arr.append(left[l])
            l += 1
    while r < len(right):
        if r < len(right):
            arr.append(right[r])
            r += 1
    return arr


def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]

    return merge(mergeSort(left),
                 mergeSort(right)
                 )


print(*mergeSort(arr))
