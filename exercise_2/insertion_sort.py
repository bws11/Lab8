def insertion_sort(arr: list) -> list:
    # Start with the second value
    # repeated move that value left until it's in the right place
    # Repeat
    
    total_swaps: int = 0
    for i in range(1, len(arr)):
        new_index = i

        for _ in range(0, i): # no var needded
            if arr[new_index] <= arr[new_index - 1]:
                arr[new_index], arr[new_index - 1] = arr[new_index - 1], arr[new_index]
                
                new_index = new_index - 1
                total_swaps += 1
                
                print("Array:", arr)
    
    print("Total swaps:", total_swaps)
    return arr

