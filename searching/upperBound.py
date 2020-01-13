print("Enter a sorted array")
arr = list(map(int, input().split()))
print("Enter the element you want to find")
k = int(input())

def upperBound(arr, k, l, r):
    upper = -1
    while l <= r:
        mid = (l+r)//2

        if arr[mid] == k:
            upper = mid
            l = mid+1
        
        elif arr[mid] > k:
            r = mid - 1

        else:
            l = mid+1

    return upper

value = upperBound(arr, k, l, r)

if value == -1:
    print("The element is not present in the given array")
else:
    print("Upper bound of the element is at", value)