def solution(A):
    """
    A function that, given an array A - consisting of N different integers in the range [1..(N + 1)], returns the value of the missing element.
    For example, given array A such that:
    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
    the function should return 4, as it is the missing element.
    """
    # Define a variable to store the previous element in an iteration
    previous_int = 1

    # Sort the list
    A.sort()

    for el in A[1:]:
        if el - previous_int == 2:
            return el-1
        previous_int = el


def solution2(A):
    """
    Similar to solution(), but without using sort().
    """
    # Define a variable to store the previous element in an iteration
    previous_int = 1

    while True:
        if previous_int+1 in A:
            previous_int += 1
            continue
        else:
            return previous_int+1
