# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 맵 정보 입력받기
graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) :
    # 범위를 벗어나면 False 출력
    if x <= -1 or x >= m or y <= -1 or y >= m :
        return False
    if graph[x][y] == 0 :
        # 현재 노드를 1로 바꿈
        graph[x][y] = 1
        # 연결된 모든 노드(중 0이 있다면)를 1로 바꿈
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    # 현재 노드가 0이라면 False 출력
    return False

# 모든 노드에 대하여 DFS 수행
result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True :
            result += 1

print(result)
