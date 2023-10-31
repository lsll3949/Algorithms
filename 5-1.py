INF = float('inf')
D = [[0, 4, 2, 5, INF], [INF, 0, 1, INF, 4], [1, 3, 0, 1, 2], [-2, INF, INF, 0, 2], [INF, -3, 3, 1, 0]]
N = len(D) # 그래프 정점 수
pred = [[-1 for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                pred[i][j] = k
print("최단 거리")
for i in range(N):
    for j in range(N):
        print('%3d' % D[i][j], end='')
    print()
print("pred")
for i in range(N):
    for j in range(N):
        if pred[i][j] != -1:
            print('%3d' % pred[i][j], end='')
        else:
            print(' -', end='')
    print()