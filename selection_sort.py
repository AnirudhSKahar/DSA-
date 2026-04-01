# selection sort code 
def selection(arr):
    n=len(arr)
    for i in range (n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
            arr[i],arr[mini]=arr[mini],arr[i]


arr=[7,5,8,4,2,1,6,3]
selection(arr)
print("sorted array is:",arr)            
            