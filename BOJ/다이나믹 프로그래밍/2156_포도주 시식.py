# 포도주 시식
# 규칙
    # 포도주 잔 선택 -> 그 잔 포도주 모두 마셔야함, 마신 후 원래 위치에
    # 연속으로 놓여있는 3잔을 모두 마실 수는 없음
# 1~N까지 포도주잔이 순서대로 테이블위에 놓여있음
# 각 포도주 잔에 들어있는 포도주의 양 -> 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램

# 입력 : 포도주 잔의 개수 N(1~10000)
# n개의 줄에 포도주 잔에 들어있는 포도주의 양(0~1000)
# 출력 : 최대로 마실 수 있는 포도주의 양

# 점화식 : d[n] = max( d[n-1]+Wn , d[n-2]+Wn , d[n-1])
            #  = max( d[n-3]+Wn-1+Wn , d[n-2]+Wn , d[n-1])
# -> 자기자신을 포함하지 않아도 됨

import sys
n=int(sys.stdin.readline())
wine=[0]
for i in range(n):
    wine.append(int(sys.stdin.readline()))

d=[0]*(1+n)
d[1]=wine[1]
if n>=2:
    d[2]=wine[1]+wine[2]

    for i in range(3,n+1):
        d[i]=max(d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i],d[i-1])

# print(d)
print(max(d))

# 6
# 6
# 10
# 13
# 9
# 8
# 1       # 33

# 6
# 1
# 2
# 3
# 4
# 5
# 6       # 16

# 6
# 1000
# 1000
# 1
# 1
# 1000
# 1000    # 4000