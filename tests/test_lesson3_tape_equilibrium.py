from solutions.lesson3_tape_equilibrium import solution


def test_array_of_positive_integers():
    assert solution([3, 1, 2, 4, 3]) == 1


def test_array_of_negative_integers():
    assert solution([-3, -1, -2, -4, -3]) == 1


def test_array_of_mixed_integers():
    assert solution([-3, 1, 2, -4, 3]) == 1
