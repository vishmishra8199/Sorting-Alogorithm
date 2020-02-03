def insertion_sort(arr):
    for i in range(1,len(arr)):
        k=arr[i]
        j=i-1
        while(j>=0 and arr[j]>k):
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=k

    return arr

print(insertion_sort([5,3,0,7,1,34,98,55]))

# best case O(n), average case O(n^2), worst case O(n^2)
