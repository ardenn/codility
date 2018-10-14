# Count the length of the longest binary gap given an integer N
def solution(N):
    start_count = False
    max_gap = 0
    current_gap = 0

    # Generate binary rep on N.
    while N > 0:
        if N % 2 == 1:
            if start_count:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                start_count = True
        else:
            if start_count:
                current_gap += 1
        N = int(N/2)
    return max_gap


if __name__ == '__main__':
    print(solution(7))
    print(solution(10417))
    print(solution(457))
    print(solution(107))
