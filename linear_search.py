# linear search
def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [7, 5, 8, 4, 2, 1, 6, 3]
target = 4
result = linear(arr, target)
print("the given array is ", arr, "and the target is ", target, "and the result is ", result)
arr2=[1,2,3,4,5,6,7,8,9]
target2 = 5
result2 = linear(arr2, target2)
print("the given array is ", arr2, "and the target is ", target2, "and the result is ", result2)