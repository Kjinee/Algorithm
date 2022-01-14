# N, M, A, B, d를 공백으로 구분하여 입력 받기
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 맵 정보를 입력 받기
map_data = []
for i in range(n) :
    map_data.append(list(map(int, input().split())))

direction = [0, 1, 2, 3] # 북동남서
steps = [[-1,0], [0,1], [1,0], [0,-1]] # 북동남서에 해당하는 이동

# 앞으로 한 칸 이동하는 함수
def move_forward() :
    global a, b, map_data, count, turn_time
    map_data[a][b] = 1 # 방문한 칸은 바다로 만듦
    a, b = na, nb # 한 칸 이동
    count += 1
    turn_time = 0

count = 1
turn_time = 0
while True :
    # 반시계 방향으로 회전
    d = direction[direction.index(d) - 1]
    # 이동할 장소
    na = a + steps[d][0]
    nb = b + steps[d][1]
    # 육지라면 한 칸 전진
    if map_data[na][nb] == 0 :
        move_forward()
        continue
    # 바다라면 이동 안 함
    turn_time += 1
    if turn_time == 4 :
        d = direction[direction.index(d) - 2] # 뒤로 돌기
        na = a + steps[d][0]
        nb = b + steps[d][1]
        if map_data[na][nb] == 0 :
            move_forward()
            continue
        break # 사면이 모두 바다라면 break

print(count)
