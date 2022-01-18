# 정수 N, M을 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

inf = 10001 # 계산 불가능한 경우(화폐는 최대 10000개 필요하므로)

# DP 테이블 초기화
d = [inf] * 10001

# 다이나믹 프로그래밍 (보텀업 방식)
d[0] = 0
for coin in n:
    for money in range(coin, m+1):
        if d[money - coin] != inf: # 남은 금액이 맞아 떨어지면 지불 가능
            d[money] = min(d[money], d[money-coin] + 1)

# 결과 출력
if d[m] == inf:
    print(-1)
else:
    print(d[m])
