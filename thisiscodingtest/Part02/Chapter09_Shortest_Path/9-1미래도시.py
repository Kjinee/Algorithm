# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# N, M을 입력받기
n, m = map(int, input().split())

# 회사간의 연결 정보를 나타내는 2차원 리스트 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 거리 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 회사 간의 연결 정보(=1)를 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x와 k를 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for j in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])

# 최단 거리 계산 (1->k 최단 거리 + k->x 최단 거리)
distance = graph[1][k] + graph[k][x]

if distance >= INF: # 도달할 수 없는 경우 -1 출력
    print(-1)
else: # 도달할 수 있다면 거리 출력
    print(distance)
