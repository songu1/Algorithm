# 가장 긴 바이토닉 부분 수열
# s1<s2<..<sk-1<sk>sk+1...sn-1>sn 을 만족하는 수열 : 바이토닉 수열
    # {10,20,30,40} : 바이토닉 수열 / {10,20,30,40,20,30} : 바이토닉 수열 X
# 수열 A -> 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하기

# 입력 : 수열A크기 n (1~1000)
# 수열 A를 이루는 Ai (1~1000)
# 출력 : 수열 A의 부분 수열 중 가장 긴 바이토닉 수열

import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
d1=[1]*n
d2=[1]*n

# 왼쪽부터 증가
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            d1[i]=max(d1[i],d1[j]+1)
# 오른쪽부터 증가
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if a[i]>a[j]:
            d2[i]=max(d2[i],d2[j]+1)
# d1+d2-1 중 최댓값
maxLen=0
for i in range(n):
    maxLen=max(maxLen,d1[i]+d2[i]-1)

print(maxLen)



# 10
# 1 5 2 1 4 3 4 5 2 1     # 7

# 6
# 1 5 4 6 7 9             # 5

# 1
# 3                       # 1

# 6
# 1 4 3 2 5 1             # 5

# 3
# 1 1 1                   # 1
