from insertion_sort import insertion_sort
from selection_sort import selection_sort
import pytest

def test_insertion_sort():
    assert insertion_sort([9, 4, 6, 2, 7]) == [2, 4, 6, 7, 9]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_selection_sort():
    assert selection_sort([25, 64, 11, 22, 12]) == [11, 12, 22, 25, 64]
    assert selection_sort([64, 25, 22, 12, 11]) == [11, 12, 22, 25, 64]

pytest.main()