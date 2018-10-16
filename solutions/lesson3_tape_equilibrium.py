def solution(A):
    """
    A function that, given a non-empty array A of N integers split into two non-empty parts by P, where 0<P<N, returns the minimal absolute difference between the sum of the first part and the sum of the second part, such that the difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
    For example, given:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
    We can split this array in four places:
    P = 1, difference = |3 − 10| = 7 

    P = 2, difference = |4 − 9| = 5  

    P = 3, difference = |6 − 7| = 1  

    P = 4, difference = |10 − 3| = 7  
    the function should return 1, as explained above. 
    """
    # Declare variables to keep track of current and minimum differences
    current_diff = 0
    min_diff = abs(sum(A[:1]) - sum(A[1:]))

    # Iterate through all values of P calculating difference at each stage
    for p in range(2, len(A)-1):
        current_diff = abs(sum(A[:p]) - sum(A[p:]))
        min_diff = min(current_diff, min_diff)
    return min_diff


solution([3, 1, 2, 4, 3])
