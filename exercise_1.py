def bubble_sort(arr: list):
    while True:
        changed: int = 0
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                changed += 1
        
        if changed == 0:
            break
    
    return arr


