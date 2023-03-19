# 정수 삼각형
# 삼각형의 크기 n -> 높이가 n인 삼각형
# 맨 위층부터 시작하여 아래 있는 수 중 하나를 선택하여 아래층으로 내려옴
# 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선에 있는 것 중에서만 선택 가능

# 입력 : 삼각형의 크기 n(1~500)
# n개의 줄에 정수 삼각형이 주어짐
# 출력 : 합이 최대가 되는 경로에 있는 수의 합을 출력

# 점화식 : (i-1,j-1),(i-1,j) => (i,j)
# j=0   d[i][j]=d[i-1][j]+d[i][j]
# j=i   d[i][j]=d[i-1][j-1]+d[i][j]
# else  d[i][j]=max(d[i-1][j-1], d[i-1][j]) + d[i][j]

# 입력받은 배열과 d를 같이 사용!!

import sys
n=int(sys.stdin.readline())
d=[]
for i in range(n):
    d.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            d[i][j]=d[i-1][j]+d[i][j]
        elif j==i:
            d[i][j]=d[i-1][j-1]+d[i][j]
        else:
            d[i][j]=max(d[i-1][j-1], d[i-1][j]) + d[i][j]

print(max(d[n-1]))

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5       # 30