def printer_result(P, i, j):
    if i == j:
        print('A' + str(i), end='')
    else:
        print('(', end='')
        printer_result(P, i, P[i][j])
        printer_result(P, P[i][j]+1, j)
        print(')', end='')
        
d = [10, 20, 5, 15, 30] # 입력 행렬
N = len(d)-1
C = [[0 for _ in range(N+1)] for _ in range(N+1)]
P = [[0 for _ in range(N+1)] for _ in range(N+1)]
for L in range(2, N+1):
    for i in range(1, N-L+2):
        j = i + L - 1
        C[i][j] = float('inf')
        for k in range(i, j):
            temp = C[i][k] + C[k+1][j] + d[i-1]*d[k]*d[j]
            if temp < C[i][j]:
                C[i][j] = temp
                P[i][j] = k
    for i in range(1, N+1):
        for j in range(1, N+1):
            print('%4d  ' % C[i][j], end='')
        print()
    print('최소 곱셈 횟수 =', C[1][N])
    printer_result(P, 1, N)
    print()