# binary search 
def binary_search(arr, target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
# Example usage
arr = [1, 2, 3, 6, 7, 8, 9]
target = 7
result = binary_search(arr, target)
print("the array is: ", arr, "and the target is: ", target, "and the result is: ", result)