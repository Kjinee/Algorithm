from collections import deque
import copy

# n을 입력받기
n = int(input())

cost = [0] * (n+1) # 각 강의 비용(시간) 초기화
indegree = [0] * (n+1) # 진입차수 초기화

graph = [[] for _ in range(n+1)] # 간선 정보 초기화

# 각 간선 정보를 입력받기
for i in range(1, n+1):
    array = list(map(int, input().split()))
    cost[i] = array[0]
    for x in array[1:-1]:
        # x가 i의 선수과목이 됨
        graph[x].append(i)
        indegree[i] += 1

# 위상 정렬 함수
def topology_sort():
    q = deque()
    result = copy.deepcopy(cost)

    # 진입차수가 0인 원소를 큐에 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 연결된 노드에 대해
        for i in graph[now]:
            indegree[i] -= 1 # 진입차수 제거
            result[i] = max(result[i], result[now]+cost[i]) # 수강 시간 갱신
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])

topology_sort()
