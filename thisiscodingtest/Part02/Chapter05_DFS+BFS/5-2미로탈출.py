from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))
    
# 이동할 네 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 메서드 정의
def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue :
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny>=m :
                continue
            # 0인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 마지막 노드까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
