# 특정 원소 x의 루트 노드를 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소 a, b에 union 연산을 수행하기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n, m을 입력받기
n, m = map(int, input().split())

# 부모 노드 테이블 초기화
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

edges = [] # 간선 테이블 초기화

# 모든 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort() # 비용을 기준으로 정렬

result = 0 # 유지비 초기화

# 간선을 하나씩 확인하여
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += c
        max_c = c

print(result - max_c) # 두 마을을 연결할 필요 없으므로 마지막 간선 비용 제외
