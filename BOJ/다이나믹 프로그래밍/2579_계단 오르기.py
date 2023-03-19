# 계단 오르기 - DP
# 계단 아래 시작점 -> 계단 꼭대기의 도착점
# 일정한 점수가 있는 계단을 밟으면 그 점수를 얻음
# 규칙
    # 계단은 한번에 1 or 2계단
    # 연속된 3개의 계단을 모두 밟아서는 안됨(시작점은 계단에 포함X)
    # 마지막 도착 계단은 반드시 밟아야함

# 입력 : 계단의 개수 (1~300)
# 한줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 계단에 쓰여있는 점수가 주어짐 (1~10000)
# 출력 : 계단ㅇ 오르기 게임에서 얻을 수 있는 총 점수의 최댓값

# 점화식
# d[i] = max( d[i-2]+step[i], d[i-1]+step[i] )
#      = max( d[i-2]+step[i], d[i-3]+step[i-1]+step[i])
# d[i-1] = d[i-2]+step[i-1] => 3번 연속이므로 안됨
#        = d[i-3]+step[i-1] => 가능(d[i] 점화식에 대입)

import sys

n=int(sys.stdin.readline())
step=[0]
for i in range(n):
    step.append((int(sys.stdin.readline())))

d=[0]*(n+1)
d[1]=step[1]
if n>=2:
    d[2]=step[1]+step[2]

    for i in range(3,n+1):
        d[i]=max(d[i-2]+step[i], d[i-3]+step[i-1]+step[i])

print(d[n])



# 6
# 10
# 20
# 15
# 25
# 10
# 20      # 75