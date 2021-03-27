# Knapsack 1/0 cu PD (cu values = weigths)
def Knapsack(n, k, A, B):
    if n == 0 or k == 0:
        return 0

    m = [[0 for i in range (0, k + 1)] for j in range(0, n + 1)]
    
    for i in range(0, n + 1):
        for j in range(0, k + 1):
            if j == 0 or i == 0:
                m[i][j] = 0
            else:
                if k >= B[i - 1]:
                    m[i][j] = max(m[i - 1][j], A[i - 1] + m[i - 1][j - B[i-1]])
                else:
                    m[i][j] = m[i - 1][j]

    return m[n][k]

n = int(input("Enter number of objects: "))
k = int(input("Enter weigth of knapsack: "))

W = list(map(int,input("\nEnter the weigths : ").strip().split()))[:n]

print(Knapsack(n, k, W, W))
