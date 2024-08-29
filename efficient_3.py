import sys
#from resource import *
import time
import psutil

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

test_case = 15
with open(sys.argv[1]) as file:
    lines = [line.strip() for line in file.readlines()]
s1 = lines[0]
array1 = []
s2 = ""
array2 = []
flag = True
for line in lines[1:]:
    if line.isalpha():
        flag = False
        s2 = line
        continue
    if flag:
        array1.append(int(line))
    else:
        array2.append(int(line))
    
alpha = {
    ("A", "A"): 0,
    ("A", "C"): 110,
    ("A", "G"): 48,
    ("A", "T"): 94,
    ("C", "C"): 0,
    ("C", "G"): 118,
    ("C", "T"): 48,
    ("G", "G"): 0,
    ("G", "T"): 110,
    ("T", "T"): 0
}
delta = 30

def generate_string(string, array):
    for index in array:
        string = string[:index+1] + string + string[index+1:]
    return string

s1, s2 = generate_string(s1, array1), generate_string(s2, array2)
l1, l2 = len(s1), len(s2)

def get_cost(x, y):
    tup = (x, y)
    if tup in alpha:
        return alpha[tup]
    else:
        return alpha[tup[::-1]]

def get_optimum_cost(s1, s2, l1, l2):
    row2 = [i*delta for i in range(l2+1)]
    for i in range(1, l1+1):
        row1 = [*row2]
        row2[0] += delta
        for j in range(1, l2+1):
            row2[j] = min(row1[j-1] + get_cost(s1[i-1], s2[j-1]), row2[j-1]+delta, row1[j]+delta)
    return row2

def join(s1, s2):
    ns2 = ""
    cost = 0
    if s2 in s1:
        index = s1.index(s2)
    else:
        costs = []
        for c in s1:
            costs.append(get_cost(c, s2))
        index = costs.index(min(costs))
        cost += costs[index]
    l = len(s1) - 1
    ns2 += index*"_" + s2 + (l-index)*"_"
    return (s1, ns2), l*delta+cost

def split(s1, s2):
    l1, l2 = len(s1), len(s2)

    if l2 == 0:
        gaps = len(s1)
        return (s1, "_"*gaps), gaps*delta
    elif l2 == 1:
        pair, cost = join(s1, s2)
        return pair, cost
    elif l1 == 1:
        pair, cost = join(s2, s1)
        return pair[::-1], cost
            

    l1_1 = l1//2
    half_1 = get_optimum_cost(s1[:l1_1], s2, l1_1, l2)
    half_2 = get_optimum_cost(s1[-1:l1_1-1:-1], s2[::-1], l1-l1_1, l2)
    halves = [i+j for i, j in zip(half_1, half_2[::-1])]
    splt = halves.index(min(halves))
    pair1, cost1 = split(s1[:l1_1], s2[:splt])
    pair2, cost2 = split(s1[l1_1:], s2[splt:])
    return (pair1[0]+pair2[0], pair1[1]+pair2[1]), cost1+cost2

start_time = time.time()

(as1, as2), cost = split(s1, s2)

end_time = time.time()
time_taken = (end_time - start_time)*1000


with open(sys.argv[2], "w") as file:
    file.write(f'{cost}\n{as1}\n{as2}\n{time_taken}\n{process_memory()}')