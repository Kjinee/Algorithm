import heapq

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# N, M, C를 입력받기
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)] # 각 도시의 연결 정보 리스트 초기화
time = [INF] * (n+1) # 각 도시가 메시지를 받는 데 걸리는 최소 시간 리스트 초기화

# 각 연결 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []

    # 출발지 정보 초기화
    heapq.heappush(q, (0,start))
    
    # 큐가 빌 때까지 반복
    while q:
        t, now = heapq.heappop(q)
        # 이미 방문한 적 있는 곳이면 패스
        if time[now] < t:
            continue

        # 인접한 도시들에 대해 반복
        for i in graph[now]:
            cost = t + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 실행
dijkstra(c)

count = 0 # 메시지를 받는 도시 개수
max_time = 0 # 메시지를 받는 도시 중, 가장 멀리 있는 도시와의 최단 거리

for t in time:
    if t != INF:
        count += 1
        max_time = max(max_time, t)

# 도시 개수에서 c를 제외
print(count-1, max_time)
