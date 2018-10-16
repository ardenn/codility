from solutions.lesson1_binary_gap import solution


def test_binary_gap_of_0():
    assert solution(32) == 0


def test_binary_gap_of_2():
    assert solution(9) == 2


def test_integer_with_2_binary_gaps():
    assert solution(529) == 4
