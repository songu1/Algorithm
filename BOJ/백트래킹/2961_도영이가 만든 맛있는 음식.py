# 도영이가 만든 맛있는 음식
# 재료 n개 - 각 재료의 신맛s, 쓴맛 b
# 신맛 : 곱 / 쓴맛:합
# 재료를 적절히 섞어서 신맛과 쓴맛의 차이를 최소화
# 재료는 적어도 1개 사용해야함

# 입력 : 재료의 개수 n(1~10)
# n개의 줄에 재료의 신맛과 쓴맛 (1 ~ 1,000,000,000)
# 출력 : 신맛과 쓴맛의 차이가 가장 작은 요리의 차이

import sys

n = int(sys.stdin.readline())
taste = []
for _ in range(n):
    taste.append(list(map(int,sys.stdin.readline().split())))

def backtracking(idx, s, b):
    global minDiff
    diff = abs(s-b)
    if idx != 0:
        minDiff = min(diff, minDiff)
    
    if diff == 0:
        return
    
    for i in range(idx,n):
        backtracking(i+1, s*taste[i][0], b+taste[i][1])
    return

minDiff = int(1e10)
backtracking(0,1,0)
print(minDiff)

# 1
# 3 10        # 7

# 2
# 3 8
# 5 8         # 1

# 4
# 1 7
# 2 6
# 3 8
# 4 9         # 1

# 4
# 8 9
# 1 5
# 3 7
# 2 3         # 1