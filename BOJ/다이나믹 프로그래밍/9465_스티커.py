# 스티커
# 스티커 2n개 -> 2행 n열
# 스티커를 떼면 상하좌우에 있는 스티커 사용 불가
# 스티커 점수 -> 점수의 합이 최대가 되게 스티커를 떼어내도록
# 상냥이가 뗄 수 있는 스티커의 점수의 최댓값
    # 점수의 합이 최대, 서로 변을 공유하지 않은 스티커 집합

# 입력 : 테스트케이스 수 t
# n(1~100,000)
# 2줄에 n개의 정수로 스티커의 점수 (0~100)
# 출력 : 각 테스트 케이스마다 2n개의 스티커 중 두 변을 공유하지 않는 스티커 점수의 최댓값

import sys

# 2차시도 : 성공 - 47292 KB / 936 ms
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    sticker.append([0] + list(map(int,sys.stdin.readline().split())))
    sticker.append([0] + list(map(int,sys.stdin.readline().split())))

    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    
    for i in range(2,n+1):
        blank = max(dp[0][i-2], dp[1][i-2])
        dp[0][i] = max(dp[1][i-1], blank) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], blank) + sticker[1][i]
        

    print(max(dp[0][n], dp[1][n]))

# 1차시도 : 성공 - 49048 KB / 1008 ms
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     sticker = []
#     sticker.append(list(map(int,sys.stdin.readline().split())))
#     sticker.append(list(map(int,sys.stdin.readline().split())))

#     dp = [[0]*n for _ in range(3)]
#     dp[0][0] = sticker[0][0]
#     dp[1][0] = sticker[1][0]
    
#     for i in range(1,n):
#         dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + sticker[0][i]
#         dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + sticker[1][i]
#         dp[2][i] = max(dp[0][i-1], dp[1][i-1])

#     print(max(dp[0][n-1], dp[1][n-1]))


# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80
# #
# 260
# 290