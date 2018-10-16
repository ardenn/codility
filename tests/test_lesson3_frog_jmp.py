from solutions.lesson3_frog_jmp import solution


def test_target_less_than_step():
    assert solution(10, 30, 30) == 1


def test_target_equal_to_step():
    assert solution(10, 20, 30) == 1


def test_target_greater_than_step():
    assert solution(10, 85, 30) == 3
