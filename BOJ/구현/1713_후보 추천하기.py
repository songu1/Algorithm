# 후보 추천하기
# 후보 : 일정기간동안 전체 학생의 추천에 의하여 정해진 수만큼 선정됨
# 추천받은 학생 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙
    # 1. 초기 : 모든 사진틀 비어있음
    # 2. 추천받은 학생은 반드시 사진틀에 게시
    # 3. 비어있는 사진틀이 없다면 학생 삭제 후 새롭게 추천받은 학생 게시
        # 추천수가 가장 적은 학생 삭제
        # 여러명이면 가장 오래된 학생 삭제
    # 4. 이미 게시된 학생이 추천받으면 추천수 증가
    # 5. 사진 삭제 시 추천수 0
# 사진틀의 수, 전체학생의 추천결과 (추천순) -> 최종 후보를 결정하는 프로그램

# 입력 : 사진틀 개수 n(1~20)
# 전체 학생의 총 추천 횟수(1~1000)
# 추천받은 학생을 나타내는 번호(1~100)
# 출력 : 사진틀에 거재된 최종 후보의 학생번호(오름차순)

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
student = list(map(int,sys.stdin.readline().split()))
candidate = []

for k in range(m):
    existed = False
    candidate.sort(key=lambda x:(x[1],x[2]))
    # 존재하는 후보라면 추천수 증가
    for i in range(len(candidate)):
        if student[k] == candidate[i][0]:
            candidate[i][1] += 1
            existed = True
            break
    if existed:
        continue
    if len(candidate) == n:
        del candidate[0]
    # 후보 추가
    candidate.append([student[k],1,k])

candidate.sort()

for c in candidate:
    print(c[0],end=" ")

# 3
# 9
# 2 1 4 3 5 6 2 7 2
# #
# 2 6 7

# 2
# 6
# 2 1 1 2 3 3
# #
# 1 3

# 3
# 12
# 1 5 1 1 7 5 9 9 9 5 4 6
# #
# 5 6 9