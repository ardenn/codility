from solutions.lesson2_cyclic_rotation import solution


def test_array_with_length_0_and_positive_integer_rotations():
    assert solution([], 2) == []


def test_array_with_length_0_and_0_rotations():
    assert solution([], 0) == []


def test_array_with_length_and_rotations_greater_than_0():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]


def test_array_of_same_element_and_length_greater_than_0():
    assert solution([0, 0, 0], 1) == [0, 0, 0]
