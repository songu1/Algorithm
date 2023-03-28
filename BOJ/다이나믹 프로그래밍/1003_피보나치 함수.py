# 피보나치 함수 : 재귀로(top-down 방식 : memorization)
# fibonacci(n)을 호출했을 때 0,1이 각각 몇번 출력되는지 구하는 프로그램
# fibo함수 : n번째 피보나치 수열을 구하는 함수
# 입력 : 테스트케이스 수 T
# T개의 줄에 n이 주어짐(0~40)
# 출력 : 각 테스트케이스마다 0이 출력되는 횟수, 1이 출력되는 횟수

# 메모리제이션 이용
import sys
T=int(sys.stdin.readline())

def fibo(n,d):
    if n==0:
        d[n]=[1,0]
        return d[n]
    elif n==1:
        d[n]=[0,1]
        return d[n]
    if d[n]!=[0,0]:
        return d[n]
    r1=fibo(n-1,d)
    r2=fibo(n-2,d)
    d[n][0]=r1[0]+r2[0]
    d[n][1]=r1[1]+r2[1]
    return d[n]

result=[]
for t in range(T):
    n=int(sys.stdin.readline())
    d=[[0,0] for _ in range(41)]        # 0부터 40이므로 41개 만들어줘야함***
    result.append(fibo(n,d))

for i in range(T):
    print(*result[i],sep=' ')


# 3
# 0
# 1
# 3
# # 1 0
# # 0 1
# # 1 2

# 2
# 6
# 22
# # 5 8
# # 10946 17711
