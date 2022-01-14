# N, M, K, 수열을 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort() # 입력받은 수 정렬
max1 = nums[N-1] # 가장 큰 수
max2 = nums[N-2] # 두 번째로 큰 수

# 최대 합 계산
result = (max1*K + max2) * (M // (K+1))
result += max1 * (M % (K+1))

print(result)
