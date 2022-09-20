def insertion_sort(arr):

    n = len(arr)

    for j in range(1, n):
        key = arr[j]
        i = j-1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
