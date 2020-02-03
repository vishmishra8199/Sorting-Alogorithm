def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[j],arr[i]=arr[i],arr[j]

    return (arr)

print(selection_sort([5,3,0,7,1,34,98,55]))

# best case O(n^2), average case O(n^2), worst case O(n^2)
