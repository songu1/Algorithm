# 루팡 : 배낭 하나 메고 은행 금고에 들어옴, 전동톱으로 잘려진 무게만큼의 가치를 가지는 귀금속
# 금고 안 : 귀금속 덩어리 / 배낭에선 wkg까지 담을 수 있음
# 각 금속의 무게, 무게당 가격 -> 배낭을 채울 수 있는 가장 값비싼 가격
# 입력 : 배낭의 무게 w, 귀금속의 종류 n
# i+1번째 줄에 i번째 금속의 무게 mi, 무게당 가격 pi가 주어짐
# 배낭에 담을 수 있는 가장 비싼 가격 출력

import sys

w,m=map(int,sys.stdin.readline().split())
jewel=[]
for i in range(m):
    jewel.append(list(map(int,sys.stdin.readline().split())))

jewel.sort(key=lambda x:-x[1])

cost=0
for i in range(m):
    if w>jewel[i][0]:
        cost += jewel[i][0]*jewel[i][1]
        w-=jewel[i][0]
    elif w<=jewel[i][0]:
        cost += w*jewel[i][1]
        w=0
        break

print(cost)