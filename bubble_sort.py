# making bubble sort funtion 
def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        
        
        if not swapped:
            break
    

arr=[5,4,3,2,1]         
bubble(arr)
print("sorted array is:",arr)   