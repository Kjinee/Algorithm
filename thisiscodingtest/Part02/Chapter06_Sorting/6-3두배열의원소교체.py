# n과 k를 입력받기
n, k = map(int, input().split())
# 배열 A, B의 모든 원소를 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 A, B를 각각 오름차순, 내림차순 정렬
a.sort()
b.sort(reverse=True)

# 첫 번째 인덱스부터 최대 K까지 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작으면 서로 교체
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break

print(sum(a))
