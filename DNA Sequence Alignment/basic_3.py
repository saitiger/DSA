import sys
#from resource import *
import time
import psutil

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

#test_case = 14
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

def get_cost(x, y):
    tup = (s1[x-1], s2[y-1])
    if tup in alpha:
        return alpha[tup]
    else:
        return alpha[tup[::-1]]

def generate_string(string, array):
    for index in array:
        string = string[:index+1] + string + string[index+1:]
    return string

s1, s2 = generate_string(s1, array1), generate_string(s2, array2)
l1, l2 = len(s1), len(s2)

start_time = time.time()

array = [[(0 if i !=0 and j!=0 else i+j)*delta for j in range(l2+1)] for i in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        array[i][j] = min(array[i-1][j-1] + get_cost(i, j), array[i-1][j]+delta, array[i][j-1]+delta)

i, j = l1, l2
as1, as2 = "", ""
while i != 0 or j != 0:
    x_y_, x_, y_ = array[i-1][j-1] + get_cost(i, j), array[i-1][j]+delta, array[i][j-1]+delta
    if x_y_ <= x_ and x_y_ <= y_:
        i -= 1
        j -= 1
        as1 += s1[i]
        as2 += s2[j]
    elif x_ <= x_y_ and x_ <= y_:
        i -= 1
        as1 += s1[i]
        as2 += "_"
    else:
        j -= 1
        as2 += s2[j]
        as1 += "_"

end_time = time.time()
time_taken = (end_time - start_time)*1000

with open(sys.argv[2], "w") as file:
    file.write(f'{array[-1][-1]}\n{as1[::-1]}\n{as2[::-1]}\n{time_taken}\n{process_memory()}')
