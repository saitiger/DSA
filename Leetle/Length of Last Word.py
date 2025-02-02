def solve(s):
    s = s.rstrip()  # Remove trailing spaces
    cnt = 0
    for i in range(len(s) - 1, -1, -1):  
        if s[i] != " ":
            cnt += 1
        elif cnt > 0:  
            return cnt
    return cnt  # Return the count if we reach the beginning {For the case when there is only one word}
