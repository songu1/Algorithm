# RGB거리 - 풀이 참고**** 점화식 생각하는 것이 중요!!!
# RGB 거리에는 1~N번 집이 있음, 거리는 선분
# 집을 빨, 초, 파 중 하나로 칠해야함
# 규칙 : 이웃한 집은 색이 달라야함
# 각각의 집을 빨,초,파로 칠하는 비용 -> 모든 잡을 칠하는 비용의 최솟값

# 입력 : 집의 수 n(2~1000)
# n개의 줄에 각 집을 빨, 초, 파로 칠하는 비용이 한줄씩 (1~1000)
# 출력 : 모든 집을 칠하는 비용의 최솟값

# R:0 / G:1 / B:2
# d[i][r/g/b] = d[i-1][r/g/b](R/G , R/B, G/B) + R,G,B 비용

import sys

n=int(sys.stdin.readline())
houses=[[]]
for i in range(n):
    houses.append(list(map(int,sys.stdin.readline().split())))

for i in range(2,n+1):
    # i번째 R
    houses[i][0]=min(houses[i-1][1],houses[i-1][2])+houses[i][0]
    # i번째 G
    houses[i][1]=min(houses[i-1][0],houses[i-1][2])+houses[i][1]
    # i번째 B
    houses[i][2]=min(houses[i-1][0],houses[i-1][1])+houses[i][2]

print(min(houses[n]))

# 3
# 26 40 83
# 49 60 57
# 13 89 99        # 96

# 3
# 1 100 100
# 100 1 100
# 100 100 1       # 3

# 3
# 1 100 100
# 100 100 100
# 1 100 100       # 102

# 6
# 30 19 5
# 64 77 64
# 15 19 97
# 4 71 57
# 90 86 84
# 93 32 91        # 208

# 8
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19        # 253