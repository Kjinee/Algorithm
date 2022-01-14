# 현재 나이트의 위치 입력받기
x, y = input()

x = ord(x) - ord('a') + 1
y = int(y)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

# 8가지 방향에 대하여 각 위치로 이동할 수 있는지 확인
count = 0
for steps in steps:
    # 이동하고자 하는 위치 확인
    nx = x + step[0]
    ny = y + step[1]
    # 해당 위치로 이동할 수 있다면 카운트 증가
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8 :
        count += 1

print(count)
