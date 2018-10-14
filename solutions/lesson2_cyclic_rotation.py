def solution(A, K):
    """
    A function that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
    For example, given
        A = [3, 8, 9, 7, 6]
        K = 3
    the function should return [9, 7, 6, 3, 8]. Three rotations were made:
        [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
        [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
        [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    """
    # Check if array not empty, and pop the last element, then insert it at the beginning
    if len(A) > 0:
        for _ in range(K):
            A.insert(0, A.pop())
    return A


if __name__ == '__main__':
    print(solution([3, 8, 9, 7, 6], 3))
