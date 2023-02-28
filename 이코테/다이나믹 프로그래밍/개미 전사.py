# 개미전사 -> 풀이 참고
# 개미 전사가 메뚜기 마을의 식량 창고를 몰래 공격 (식량창고는 일직선으로)
# 각 식량창고에는 정해진 수의 식량을 저장, 개미전사가 식량창고를 선택적으로 약탈
# 메뚜기 정찰병들은 일직선 상에 존재하는 식량 창고 중 서로 인접한 창고가 공격받으면 알아차림
# 개미전사가 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야함
# 식량창고 N에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값

# 입력 : 식량창고 개수 n (3 <= n <=100)
# 각 식량창고에 저장된 식량의 개수 k (0 <= k <= 1000)
# 출력 : 개미전사가 얻을 수 있는 식량의 최댓값

# 예시
# 1 3 1 5 -> 2,4번째 식량 창고 선택 시 최대값인 8개의 식량을 뺏음

import sys

n=int(sys.stdin.readline())
warehouse=list(map(int,sys.stdin.readline().split()))
result=[0]*n

result[0]=warehouse[0]
result[1]=max(warehouse[0],warehouse[1])

for i in range(2,n):
    result[i]=max(result[i-1],result[i-2]+warehouse[i])

print(result[n-1])

# 4
# 1 3 1 5         # 8