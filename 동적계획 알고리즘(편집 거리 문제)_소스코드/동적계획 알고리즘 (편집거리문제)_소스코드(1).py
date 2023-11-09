S = list('strong')
T = list('stone')
N = len(S)
M = len(T)
E = [[0 for _ in range(M+1)] for _ in range(N+1)]
E[0] = [i for i in range(M+1)] # 첫번째 행 초기화
for i in range(N+1): # 첫번째 열 초기화
    E[i][0] = i

for i in range(1, N+1):
    for j in range(1, M+1):
        alpha = 0 if S[i-1] == T[j-1] else 1
        E[i][j] = min(E[i][j-1]+1, E[i-1][j]+1, E[i-1][j-1]+alpha)
        
print('최종 배열: E')
for i in range(N+1): 
    for j in range(M+1):
        print(' ', E[i][j], end='')
    print()
print('편집 거리 = ', E[N][M])