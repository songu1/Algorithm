# 행복 유치원
# n명의 원생들을 일렬로 줄 세우고 k개의 조로 나눔
# 각 조에는 원생이 1명 이상 있어야함, 같은 조에 속한 원생들은 인접
# 조별로 단체 티셔츠 비용 : 가장 큰 원생의 키 - 가장 작은 원생의 키
# k개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고싶어함

# 입력 : 유치원 원생 수 n(1~300,000), 조의 개수 k(1~n)
# 원생들의 키(오름차순) (1~10e9)
# 출력 : 티셔츠 만드는 비용이 최소가 되도록 k개으 조를 나누었을 때 티셔츠 만드는 비용

import sys

n,k = map(int,sys.stdin.readline().split())
children = list(map(int,sys.stdin.readline().split()))
dif = []
for i in range(len(children)-1):
    dif.append(children[i+1]-children[i])
dif.sort()
cost = sum(dif[:n-k])

print(cost)

# 5 3
# 1 3 5 6 10          # 3