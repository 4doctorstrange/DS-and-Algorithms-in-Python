import math
def greedy(weight, values, capacity):
    res=0
    for i in sorted(zip(weight, values), key = lambda x: x[1]/x[0],reverse=True):
        if i[0] >capacity:
            fraction=capacity/i[0]
            res+=fraction*i[1]
            break
        if capacity-i[0]>=0:
            res+=i[1]
            capacity-=i[0]
    return res

weights = [10, 40, 20, 30]
values = [60, 40, 100, 120]
capacity = 50
print(greedy(weights, values, capacity))