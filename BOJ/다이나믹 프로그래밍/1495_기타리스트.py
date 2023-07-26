# 기타리스트
# 공연에서 연주할 n개의 곡을 매번 곡이 시작하기전 볼륨을 바꾸고 연주
# 각각의 곡이 시작하기 전 바꿀 수 있는 볼륨 리스트 V
    # V[i] : i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨
# 볼륨 : P + V[i] or P - V[i]
    # 볼륨은 0이상 M이하
# 곡 개수 n, 시작 볼륨 s, m -> 마지막 곡을 연주할 수 있는 볼륨 중 최댓값

# 입력 : n(1~50), s(0~m), m (1~1000)
# 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이 (1~m)
# 출력 : 가능한 마지막 곡의 볼륨 중 최댓값(마지막 곡 연주 불가능 -> -1)

# 2차 시도
import sys

n,s,m = map(int,sys.stdin.readline().split())
v = list(map(int,sys.stdin.readline().split()))
v.insert(0,0)

dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][s] = True

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] == True:
            plus = j + v[i]
            minus = j - v[i]
            if 0 <= plus <= m:
                dp[i][plus] = True
            if 0 <= minus <= m:
                dp[i][minus] = True

result = -1
for i in range(m,-1,-1):
    if dp[n][i] == True:
        result = i
        break
print(result)

# 3 5 10
# 5 3 7           # 10

# 4 8 20
# 15 2 9 10       # -1

# 14 40 243
# 74 39 127 95 63 140 99 96 154 18 137 162 14 88      # 238



# 1차시도 : 메모리 초과 - dvol 배열이 문제인듯
# import sys

# n,s,m = map(int,sys.stdin.readline().split())
# v = list(map(int,sys.stdin.readline().split()))
# v.insert(0,0)

# dp = [-1]*(n+1)
# dvol = [[] for _ in range(n+1)]

# dp[0] = s
# dvol[0].append(s)

# for i in range(1,n+1):
#     for dv in dvol[i-1]:
#         high = dv + v[i]
#         low = dv - v[i]
#         # high O
#         if 0 <= high <= m:
#             dp[i] = max(dp[i], high)
#             dvol[i].append(high)
#             # high O, low O
#             if 0 <= low <= m:
#                 dvol[i].append(low)
#         # high X , low O
#         elif 0 <= low <= m:
#             dp[i] = max(dp[i],low)
#             dvol[i].append(low)
# print(dp[n])