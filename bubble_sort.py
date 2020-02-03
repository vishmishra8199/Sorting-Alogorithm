def buuble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
print(buuble_sort([5,3,0,7,1,34,98,55]))

# best case O(n), average case O(n^2), worst case O(n^2) 

