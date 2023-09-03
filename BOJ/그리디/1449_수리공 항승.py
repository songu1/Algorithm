# 수리공 항승
# 왼쪽에서 정수만큼 떨어진 거리만 물이 샘
# 길이가 l인 테이프 무한개 가지고 있음
# 테이프를 이용하여 물을 막음
    # 그 위치의 좌우 0.5마늠 간격을 줘야 물이 안샘
# 물이 새는 곳의 위치 , 테이프의 길이 l => 필요한 테이프의 최소 개수를 구하는 프로그램
# 테이프 자를 수 없음, 겹쳐서 붙이는 것은 가능

# 입력 : 물이 새는 곳의 개수 n, 테이프의 길이 l
# 물이 새는 곳의 위치 (1~1000)
# 출력 : 항승이가 필요한 테이프 개수

import sys

n,l = map(int,sys.stdin.readline().split())
leak = list(map(int,sys.stdin.readline().split()))
leak.sort()

tape = 0
start = -1
for lk in leak:
    if lk < start:
        continue
    tape += 1
    start = lk + l
print(tape)

# 4 2
# 1 2 100 101     # 2

# 4 3
# 1 2 3 4         # 2

# 3 1
# 3 2 1           # 3