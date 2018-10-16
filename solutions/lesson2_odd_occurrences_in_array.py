def solution(A):
    """
    A function that given a non-empty array A containing an odd number (N) of elements - all integers, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired, returns the value of the unpaired element.
    For example, given array A such that:
    A[0] = 9  A[1] = 3  A[2] = 9
    A[3] = 3  A[4] = 9  A[5] = 7
    A[6] = 9
    the function should return 7
    """
    # Define a dictionary to keep value-count pairs
    value_dict = {}
    # Define a variable to store the value with an odd count
    odd_value = None

    # Loop through A taking note of the current element's count
    for el in A:
        if el in value_dict:
            value_dict[el] += 1
        else:
            value_dict[el] = 1
        odd_value = el if value_dict[el] % 2 == 1 else odd_value
    return odd_value
