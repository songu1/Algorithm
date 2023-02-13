# A, B가 서로 무게가 다른 볼링공을 고름
# 볼링공 n개, 볼링공마다 무게가 적혀있음
# 공 번호 1번부터 ~ / 같은 무게의 공이 있어도 서로 다른공으로 간주
# 공의 무게 1~m

# 볼링공의 개수 n, 공의 최대 무게 m
# 각 볼링공의 무게 k가 순서대로 자연수 형태로

# 두 사람이 볼링공을 고르는 경우의 수(조합)

# 알고리즘
# 조합 사용
# 값이 같은 값은 제외하고 count


import sys
from itertools import *

n,m=map(int,sys.stdin.readline().split())
weight=list(map(int,sys.stdin.readline().split()))

# itertools 라이브러리의 조합 사용
cases=list(combinations(weight,2))

# 서로 다른 조합만 count
count=0
for (a,b) in cases:
    if a!=b:
        count+=1

print(count)


# 5 3
# 1 3 2 3 2           # 8

# 8 5
# 1 5 4 3 2 4 5 2     # 25