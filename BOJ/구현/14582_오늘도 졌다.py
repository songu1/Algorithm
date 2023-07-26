# 오늘도 졌다
# 역전패 : 불펜 투수
# 역전패X : 타자, 선발 투수
# 오늘 경기에서 울림 제미니스가 역전패를 했는지 구하는 프로그램
    # 경기 도중 울림 제미니스가 이기고 있는 순간이 있어야함

# 입력 : 우리팀이 낸 득점(1~9회 초)
# 상대팀이 낸 득점 (1~9회 말)
    # 한팀이 한회에 낸 득점 (0~20)
    # 상대팀의 총 득점이 더 많음
# 출력 : 역전패 : Yes / 역전패X : No

# 3분 30초 추가

import sys

woolim = list(map(int,sys.stdin.readline().split()))
start = list(map(int,sys.stdin.readline().split()))
wsum = 0
ssum = 0
result = "No"

for i in range(9):  # i회
    wsum += woolim[i]
    if wsum > ssum:
        result = "Yes"
        break
    ssum += start[i]
    if wsum > ssum:
        result = "Yes"
        break

print(result)



# 1 0 0 0 0 0 2 2 1
# 0 0 3 0 0 0 0 1 4       # Yes

# 0 0 0 0 0 0 0 1 0
# 1 0 0 0 0 0 0 4 0       # No