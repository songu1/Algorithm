# 2 X n 타일링 -> 풀고나서 풀이보기
# 2Xn 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수

# 입력: n (1~1000)
# 출력 : 2*n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지

# 규칙 : 1 2 로 시작, 이후 피보나치 수열처럼
    # a[i]=a[i-1]+a[i-2]

import sys
n=int(sys.stdin.readline())
d=[0]*1001
d[1]=1
d[2]=2

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n]%10007)






# 2       # 2
# 9       # 55
