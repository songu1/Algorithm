# 평범한 배낭
# 여행에 필요하다고 생각하는 n개의 물건
# 무게 w, 가치 v
# 준서 최대 k만큼의 무게만을 넣을 수 있는 배낭만 들고다닐 수 있음
# 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건 가치의 최댓값

# 입력 : 물품의 수 n(1~100), 준서가 버틸 수 있는 무게 k(1~100,000)
# 각 물건의 무게 w(1~100,000), 해당 물건의 가치 v(0~1000)
# 출력 : 배낭에 넣을 수 있는 물건들의 가치합의 최댓값

# 최대 k -> k 이하면 됨

import sys

# 풀이 1 - 229220KB / 4704ms
n,k = map(int,sys.stdin.readline().split())
item = [(0,0)]
d = [[0]*(k+1)]
for i in range(n):
    w,v = map(int,sys.stdin.readline().split())
    if w > k:
        continue
    item.append((w,v))
    d.append([0]*(k+1))

for i in range(1,len(item)):
    w = item[i][0]
    v = item[i][1]
    for j in range(1,k+1):
        if j>=w:
            d[i][j] = max(d[i-1][j], v + d[i-1][j-w])
        else:
            d[i][j] = d[i-1][j]

print(d[-1][-1])

# 풀이2 - 35108KB / 4028ms
n,k = map(int,sys.stdin.readline().split())
item = []
d = [0]*(k+1)
for i in range(n):
    w,v = map(int,sys.stdin.readline().split())
    if w > k:
        continue
    item.append((w,v))

for (w,v) in item:
    for i in range(k,0,-1):
        if i>=w:
            d[i] = max(d[i], v + d[i-w])
print(d[k])



# 4 7
# 6 13
# 4 8
# 3 6
# 5 12        #14

# 6 9
# 6 13
# 4 8
# 3 6
# 5 12
# 4 11
# 1 3         # 23

# 15 100000
# 61803 5
# 62863 0
# 41632 3
# 12794 2
# 71324 8
# 55358 2
# 34870 8
# 41590 7
# 17928 0
# 24218 3
# 18426 0
# 65130 2
# 16478 2
# 93173 9     # 17

# 1 2
# 1 3         # 3

# 4 2
# 1 1
# 5 1
# 5 1
# 1 2         # 3

# 6 9
# 1 3
# 3 6
# 4 11
# 4 8
# 5 12
# 6 13