import random
from exercise_1.bubble_sort import bubble_sort
from exercise_2.insertion_sort import insertion_sort
from exercise_2.selection_sort import selection_sort

test_array = random.sample(range(1, 200), 20)
test_array2 = test_array
test_array3 = test_array
print("Test array:", test_array)

print("\nBubble sort ----------------------------------------")
bubble_sort(test_array)
print("\nInsertion sort -------------------------------------")
insertion_sort(test_array2)
print("\nSelection sort -------------------------------------")
selection_sort(test_array3)
print("All tests done")