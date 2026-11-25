def selection_sort(arr: list) -> list:
    # Find the smallest number and add it to the arr
    sorted_arr: list = []
    swaps: int = 0
    while len(arr) > 0:
        smallest = min(arr) # smallest
        
        sorted_arr.append(smallest)
        arr.remove(smallest)
        swaps += 1
        
        print("Array:", sorted_arr)

    print("Total swaps:", swaps)
    return sorted_arr


if __name__ == '__main__':
    selection_sort([9, 4, 6, 2, 7])