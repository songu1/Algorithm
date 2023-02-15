# 정수 n,k 입력 
# -> 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중 k이 하나라도 포함되는 모든 경우의 수
# k가 하나라도 포함 -> 카운트
# k가 아예 없음 -> 카운트 X
# 01시 01분 01초 -> 0이 포함된 것임!!

# 입력 : n (0 <= n <= 23)
# 출력 : 모든 경우의 수 출력(개수)


import sys
h,m = map(int,sys.stdin.readline().split())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if str(m) in str(i).zfill(2)+str(j).zfill(2)+str(k).zfill(2):
                count+=1
print(count)

# 5 3     # 11475
# 3 0     # 14400