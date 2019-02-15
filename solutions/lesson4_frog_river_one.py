def solution(A, X):
    """
    A function that, given a non-empty array A consisting of N integers and integer X, returns the earliest index at which all positions from 1 to X have been filled.
    If not all positions are filled, the function should return −1.
    For example, given X = 5 and array A such that:
    A[0] = 1
    A[1] = 3
    A[2] = 1
    A[3] = 4
    A[4] = 2
    A[5] = 3
    A[6] = 5
    A[7] = 4
    the function should return 6, as explained above.
    """
    # Define a set to store filled positions
    filled_positions = set()

    # Iterate through the array, filling in the positions based on the current elements
    for index, el in enumerate(A):
        filled_positions.add(el)
        if len(filled_positions) == X:
            return index
    else:
        return -1
