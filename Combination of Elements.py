from itertools import combinations
def find_combintaion(k,n):
    list_num = []
    comb = combinations([x for x in range(1, n+1)],k)
    print(comb)
