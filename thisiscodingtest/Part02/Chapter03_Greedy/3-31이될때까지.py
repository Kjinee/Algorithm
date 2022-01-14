# N, K를 공백으로 구분하여 입력받기
N, K = map(int, input().split())

result = 0
while N > 1 :
    # N이 K의 배수가 되도록 1을 빼주기
    result += (N % K)
    
    # N을 K로 나누기
    N //= K
    result += min(N, 1) # 몫이 0이면 계산 횟수에 포함하지 않도록 함

print(result)
