def solution(X, Y, D):
    """
    A function that, given three integers X, Y and D, returns the minimal number of jumps of length D from position X to a position equal to or greater than Y.
    For example, given:
    X = 10
    Y = 85
    D = 30
    the function should return 3, because the frog will be positioned as follows:
    after the first jump, at position 10 + 30 = 40
    after the second jump, at position 10 + 30 + 30 = 70
    after the third jump, at position 10 + 30 + 30 + 30 = 100
    """
    exact_steps = (Y - X)/D
    return exact_steps if type(exact_steps) == int else int(exact_steps+1)
