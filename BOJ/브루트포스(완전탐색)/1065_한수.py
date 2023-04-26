# 한수
# 어떤 양의 정수 x의 각 자리가 등차수열을 이룸 -> 한수
    # 등차수열 : 연속된 두개의 수의 차이가 일정한 수열
# n -> 1~n에서 한수의 개수를 출력

# 입력 : n(1~1000) - 1000은 무조건 한수 아님(999까지라 생각해도 됨)
# 출력 : 1~n에 있는 한수의 개수

# 1~99 : 모두 다 한수
# 111, 123, 135, 147, 159, 210

import sys

n=int(sys.stdin.readline())
count=0
if n<100:
    count=n
else:
    count+=99   # 1~99까지의 수
    # 1000은 한수가 아니므로 999까지
    if n==1000: n=999
    # 100부터 카운트
    for num in range(100,n+1):
        c = num%10
        b = (num%100 - c) // 10
        a = num // 100
        if (a-b)==(b-c):
            count+=1

print(count)


# 110     # 99

# 1       # 1

# 210     # 105

# 1000    # 144

# 500     # 119