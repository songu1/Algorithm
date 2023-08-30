# 공주님의 정원
# n개의 꽃 : 모두 같은해에 피어서 같은해에 짐
# 하나의 꽃은 피는날과 지는날이 정해져있음
# 1,3,5,7,8,10,12 : 31일
# 4,6,9,11 : 30일
# 2 : 28일
# 조건
  # 꽃은 피는날 ~ 지는날-1 까지 피어있음 :*****문제 똑바로 읽기*****
  # 3월 1일~11월 30일 : 매일 꽃이 1가지 이상 피어있도록
  # 정원의 꽃수 최소한으로
# n개의 꽃들 중 3/1~11/30 매일 꽃이 한가지 이상 피어있도록 선택 : 선택한 꽃들의 최소개수 출력
  # 3.01 ~ 12.01까지

# 입력 : n (1~100,000)
# n개의 줄에 꽃이 피는날짜 월,일 / 꽃이 지는날짜 월 일
# 출력 : 선택한 꽃들의 최소개수 (두조건을 만족하는 꽃을 선택할 수 없으면 0)

# 1차시도 : 1%에서 틀림

import sys

n = int(sys.stdin.readline())
flower = []
for _ in range(n):
  m1,d1,m2,d2 = map(int,sys.stdin.readline().split())
  start = m1+d1*0.01
  end = m2+d2*0.01
  if end <= 3.01 or start >= 12.01:
    continue
  elif start < 3.01:
    start = 3.01
  elif end > 12.01:
    end = 12.01
  flower.append([start,end])    # 비교하기 쉽게 월을 정수, 일을 소수점 2자리로 나타내 합함
# print(*flower,sep="\n")

flower.sort(key=lambda x:x[0])

result = []
start = flower[0][0]
end = flower[0][1]
del flower[0]
if start > 3.01:
  print(0)
else:
  result.append((start,end))
  for start,end in flower:
    plant = False
    for i in range(len(result)-1,-1,-1):
      rstart = result[i][0]
      rend = result[i][1]
      if rstart == start and rend < end:
        result.pop()
        plant = True
      elif rstart < start and rend < end and rend >= start:
        if i<len(result)-1:
          for j in range(len(result)-1,i,-1):
            result.pop()
        plant = True
      if not plant:
        break

    if plant:
      result.append((start,end))
    # print(result)

  if result[-1][1] < 12.01:
    print(0)
  else:
    print(len(result))

# 4
# 1 1 5 31
# 1 1 6 30
# 5 15 8 31
# 6 10 12 10      # 2

# 10
# 2 15 3 23
# 4 12 6 5
# 5 2 5 31
# 9 14 12 24
# 6 15 9 3
# 6 3 6 15
# 2 28 4 25
# 6 15 9 27
# 10 5 12 31
# 7 14 9 1        # 5

# 3
# 3 1 5 5
# 5 5 10 8
# 10 7 11 30      # 0

# 5
# 3 1 5 1
# 4 1 12 1
# 5 1 7 1
# 7 1 9 1
# 9 1 12 1        # 4
