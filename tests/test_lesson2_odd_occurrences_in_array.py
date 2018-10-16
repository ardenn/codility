from solutions.lesson2_odd_occurrences_in_array import solution


def test_multiple_pairs_of_same_element():
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7


def test_single_pairs_of_same_element():
    assert solution([9, 3, 8, 3, 8, 7, 9]) == 7
