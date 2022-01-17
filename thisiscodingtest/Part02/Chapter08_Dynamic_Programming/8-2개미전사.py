# 정수 N, 식량 정보 K 입력받기
n = int(input())
k = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * n
d[0] = k[0]
d[1] = k[1]

# 다이나믹 프로그래밍 진행 (보텀업)
for i in range(2,n):
    d[i] += k[i] + max(d[0:i-1]) # 직전 칸을 제외하고 가장 큰 값 더해줌

# 최댓값 출력
result = max(d[-2], d[-1]) # 한 칸이라도 더 들르는 게 이득이므로 마지막 두 칸 중 하나가 최종 종착지임
print(result)
