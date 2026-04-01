# selection sort code 
def sinsertion(arr):
    n=len(arr)
    for i in range (1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[7,5,8,4,2,1,6,3]
sinsertion(arr)
print("sorted array is:",arr)            