# 퇴사
# n일동안 최대한 많은 상담을 하고 n+1일에 퇴사
# 하루에 하나씩 서로 다른 사람의 상담
    # 각 상담을 완료하는데 걸리는 기간(일) ti, 받을 수 있는 금액 pi
# 퇴사전까지 상담을 적절히 했을 때 백준이라 얻을 수 있는 최대 수익

# 입력 : n (1~15)
# n개의 줄에 t(1~5)와 p(1~1000)
# 출력 : 백준이가 얻을 수 있는 최대 이익

# 팁 : n=1이고 t가 1인 경우는 값이 나오지만 t가 1이 아닌 경우는 무조건 0값이 나온다.

import sys

n = int(sys.stdin.readline())
counsel = [[0,0]]      # counsel[i][0] : i일에 시작한 상담이 끝나는 날 / counsel[i][1] : 수익
for i in range(n):
    t,p = map(int,sys.stdin.readline().split())
    counsel.append([i+t,p])

d = [0]*(n+1)

for i in range(1,n+1):
    if counsel[i][0] > n:
        continue
    for j in range(i):
        if i <= counsel[j][0]:
            d[i] = max(d[i],counsel[i][1])
        else:
            d[i] = max(d[i], d[j]+counsel[i][1])
# print(d)
print(max(d))

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200       # 45

# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10        # 55

# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6         # 20

# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50        # 90