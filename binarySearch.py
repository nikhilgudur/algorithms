print("Enter a sorted array")
arr = list(map(int, input().split()))
print("Enter the element to find")

arr.sort()
k, l, r = int(input()), 0, len(arr)-1

def binarySearch(arr, k, l, r):
    if l <= r:

        mid = l + (r-l)//2

        if arr[mid] == k:
            return mid
        
        elif arr[mid] > k:
            return binarySearch(arr, k, l, mid-1)

        else:
            return binarySearch(arr, k, mid+1, r)

    else:
        return -1 

print("You number is at", binarySearch(arr, k, l, r))