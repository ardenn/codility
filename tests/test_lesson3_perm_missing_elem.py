from solutions.lesson3_perm_missing_elem import solution, solution2


def test_missing_element():
    assert solution([2, 3, 1, 5]) == 4


def test_missing_element_without_sort():
    assert solution2([2, 3, 1, 5]) == 4


def test_missing_element():
    assert solution([3, 1, 5, 7, 4, 6]) == 2


def test_missing_element_without_sort():
    assert solution2([3, 1, 5, 7, 4, 6]) == 2
