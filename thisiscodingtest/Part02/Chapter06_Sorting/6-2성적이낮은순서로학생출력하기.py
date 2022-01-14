# N을 입력받기
n = int(input())
# N명의 학생 정보를 입력받아 리스트에 저장
score = []
for i in range(n) :
    data = input().split()
    score.append((data[0], int(data[1])))

# 점수를 기준으로 정렬
score = sorted(score, key=lambda data: data[1])

# 결과 출력
for name, _ in score :
    print(name, end=' ')
