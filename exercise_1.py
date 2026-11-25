def bubble_sort(arr: list):
    total_swaps: int = 0
    while True:
        changed: int = 0
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                changed += 1; total_swaps += 1
                print("Array:", arr)
        
        if changed == 0:
            break
        
    print("Total swaps:", total_swaps)
    return arr


if __name__ == '__main__':
    bubble_sort([10, 3, 6, 2, 8, 1])