# 현재 캐릭터의 점수 n을 자릿수 기준으로 반으로 나눔
# 왼쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황

# 입력 : 점수n(자릿수는 항상 짝수)
# 출력 : LUCKY(성공) / READY(실패)

import sys

n=list(map(int,sys.stdin.readline().rstrip()))

n2=[]
for i in range(int(len(n)/2),len(n)):
    n2.append(n.pop())

if sum(n)==sum(n2):
    print('LUCKY')
else:
    print('READY')


# 123402        # LUCKY
# 7755          # READY