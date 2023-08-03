# 빗물 - **********힌트 참고함 : 시험에 나왔을때 풀어라
# 2차원 세계에 블록이 쌓여있음, 비가오면 빗물이 고임
# 비가 충분히 많이 올 때 고이는 빗물의 총량은?

# 입력 : 2차원 세계의 세로 길이h, 가로 길이 w (1~500)
# 블록이 쌓인 높이를 의미하는 정수(0~h) 제일 왼쪽부터 생김
    # 블록 내부에 빈 공간이 생길 수 없음 (바닥은 항상 막혀있음)
# 출력 : 고이는 빗물의 총량(2차원에서 한칸은 1) - 전혀 고이지 않을 경우 0

# 알고리즘
    # (1) 매 위치별로 물의 높이를 구함
    # (2) 자신의 min(오른쪽의 제일 높은 블록, 왼쪽의 제일 높은 블록) 값이 물의 높이가 됨
    # 첫번째 블록과 마지막 블록은 제외하고 수행

import sys

h,w = map(int,sys.stdin.readline().split())
block = list(map(int,sys.stdin.readline().split()))

water = 0
for i in range(1,w-1):  # i번째 블록
    # 자신의 오른쪽 제일 높은 블록
    height = min(max(block[:i]), max(block[i+1:]))
    if height > block[i]:
        water += height-block[i]
print(water)

# 4 4
# 3 0 1 4             # 5

# 4 8
# 3 1 2 3 4 1 1 2     # 5

# 3 5
# 0 0 0 2 0           # 0