from collections import deque
def print_first_negative_integer(A: List[int], N: int, k: int) -> List[int]:
    dll = deque()
    result = []
    i = 0
    j = 0

    while j < N:
        if A[j] < 0:
            dll.append(A[j])
        
        if j - i + 1 == k:
            neg = dll[0] if dll else 0
            result.append(neg)
            if A[i] < 0 and dll:
                dll.popleft()
            i += 1
        j += 1

    return result
