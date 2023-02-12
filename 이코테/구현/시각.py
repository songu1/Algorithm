# 정수 n 입력 
# -> 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수
# 3이 하나라도 포함 -> 카운트
# 3이 아예 없음 -> 카운트 X

# 입력 : n (0 <= n <= 23)
# 출력 : 모든 경우의 수 출력(개수)

# 전체 경우의 수 - 3이 존재하지 않는 경우의 수
import sys
n=int(sys.stdin.readline())
total=(n+1)*60*60

if n<3:
    not3=(n+1)*(5*9)*(5*9)
elif 3<=n<13:
    not3=n*(5*9)*(5*9)
elif 13<=n<23:
    not3=(n-1)*(5*9)*(5*9)
else:
    not3=(n-2)*(5*9)*(5*9)

print(total-not3)

# 5         # 11475

# 다른 풀이

# h=int(input())

# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count+=1
# print(count)