# 가장 긴 증가하는 부분 수열(LIS) - 병사배치하기와 비슷!!
# 수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열을 구하는 프로그램
# 예시
    # A={10,20,10,30,20,50} -> {10,20,30,50}, 길이는 4

# 입력 : 수열 A의 크기 n(1~1000)
# 수열 A를 이루고 있는 ai(1~1000)
# 출력 : 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력

# 가장 긴 증가하는 부분 수열 알고리즘(LIS)
# d[i] : array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식
    # 모든 0<=j<i에 대해서 d[i]=max(d[i],d[j]+1) if array[i]>array[j]

import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
d=[1]*n
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            d[i]=max(d[i],d[j]+1)

print(max(d))

# 6
# 10 20 10 30 20 50       # 4

# 6
# 10 20 10 30 50 20       # 4