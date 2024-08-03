def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print("Enter the elements of the array (sapace seperated): ")
arr = list(map(int, input().strip().split()))
print("Array before sorting:",arr)
result = selectionSort(arr)
print("The sorted array is:",result)