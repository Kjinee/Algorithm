# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(N) :
    cards = list(map(int, input().split()))
    rowmin = min(cards) # 현재 행의 최솟값 찾기
    result = max(result, rowmin) # 그 중 가장 큰 수 찾기

print(result)
