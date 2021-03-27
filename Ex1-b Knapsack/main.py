f = open("knapsack2.txt", "r")

k = int(f.readline())

sum = 0
x = int(f.readline())
while(x != -1):
    if (x <= k):
        sum += x
        k -= x
    elif (sum < x):
        sum = x
        break
    x = int(f.readline())

print(sum)
# am folosit 3 variabile: k, sum, x
# pentru un algoritm 1/2OPT se vor forma 2 cazuri:
# 1. sum <= k/2 astfel urmatorul element fiind k- k/2 = k/2 inlocuim suma cu acest element a. i. conditia de 1/2 este indeplinita
# 2. sum >= k/2 conditia de 1/2 fiind indeplinita