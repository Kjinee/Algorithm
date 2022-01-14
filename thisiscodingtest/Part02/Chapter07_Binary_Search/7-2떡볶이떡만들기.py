# N, M을 입력받기
n, m = map(int, input().split())
# 떡의 개별 높이를 입력받기
array = list(map(int, input().split()))

start = 0
end = max(array)

while (start <= end) :
    # 절단기의 높이
    mid = (start + end) // 2
    # 잘린 떡 길이의 합 (!!조건문 이용!!)
    rest = 0
    for x in array:
        if x > mid:
            rest += (x - mid)

    # 떡 길이가 모자라면 mid를 낮춤
    if rest < m:
        end = mid - 1
    # 떡이 충분하면 mid를 높임
    else:
        result = mid # !!마지막으로 떡이 충분했던 시점 기록!!
        start = mid + 1
        
print(result)
