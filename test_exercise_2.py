from exercise_2 import insertion_sort
import pytest

def test_insertion_sort():
    assert insertion_sort([9, 4, 6, 2, 7]) == [2, 4, 6, 7, 9]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
pytest.main()