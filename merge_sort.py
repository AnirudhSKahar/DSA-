# Merge Sort Algorithm 
# Merge Sort is a divide-and-conquer algorithm that breaks down a list into smaller sublists
# until each sublist contains a single element. Then, it merges those sublists back together in a sorted order.
# The time complexity of Merge Sort is O(n log n) in all cases (best, average, and worst), making 
# it an efficient sorting algorithm for large datasets.
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=arr[ :mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half,r_half)

# The merge function takes two sorted lists (left and right) 
# and merges them into a single sorted list. It uses two pointers (i and j)
# to keep track of the current position in each list.
# The function compares the elements at these positions and appends the smaller one to the new list, 
# moving the corresponding pointer forward. Once one of the lists is fully traversed, 
# it appends the remaining elements of the other list to the new list. Finally, 
# it returns the merged and sorted list.
def merge(left,right):
    new=[]
    i,j=0,0
    
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
            
            
            
    new.extend(left[i:])
    new.extend(right[j:])
    return new
    
            
            
arr=[9,5,4,3,5,356,56,7,8]
print (merge_sort(arr))

    