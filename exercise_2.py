def insertion_sort(arr: list):
    # Start with the second value
    # repeated move that value left until it's in the right place
    # Repeat
    

    for i in range(1, len(arr)):
        new_index = i

        for j in range(i, 0, -1):
            if arr[new_index] <= arr[j]:
                arr[new_index], arr[j] = arr[j], arr[new_index]
                new_index = j
                print(arr)
                
    return arr

insertion_sort([9, 4, 6, 2, 7])