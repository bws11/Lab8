import pytest
from bubble_sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([10, 3, 6, 2, 8, 1]) == [1, 2, 3, 6, 8, 10]
    assert bubble_sort([1, 2, 3, 4, 5]) ==  [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
pytest.main()