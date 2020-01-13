print("Enter an array:")
arr = list(map(int, input().split()))
arr.sort()
print("Enter a key you want to find")
k = int(input())
l, r = 0, len(arr)-1

def lower_bound(arr, k, l, r):
    lower = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == k:
            lower = mid
            r = mid-1
        elif arr[mid] > k:
            r = mid-1
        else:
            l = mid+1
    return lower

value =  lower_bound(arr, k, l, r)

if value == -1:
    print("Element is not present in the given array")

else:
    print("Lower Bound of the element is at", value)