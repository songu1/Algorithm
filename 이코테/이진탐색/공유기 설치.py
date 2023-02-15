# 문제 해결 중

# 공유기 설치 : 이진탐색, 파라메트릭 알고리즘 (반복문 사용하기) ** 풀이 참고
# 도현이네 집 n개가 수직선 위(x1,x2,...xn)
# 어디서나 와이파이를 즐기기 위해 집에 공유기 c개 설치
# 한 집에는 공유기 하나, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
# c개의 공유기를 n개의 집에 적당히 설치 -> 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

# 입력 : 집의 개수 n(2~20만개), 공유기의 개수 c(2~n) (n>=c)
# n개의 줄에 집의 좌표를 나타내는 xi가 한줄에 하나씩
# 출력 : 가장 인접한 두 공유기 사이의 최대거리

# 알고리즘
# 0번째 집, 마지막 집 선택 (최소2개)
# 0번째 집과 다른 집 사이의 거리로 이진탐색하기
# 예시 : [1,2,4,8,9]

# import sys
# n,c=map(int,sys.stdin.readline().split())
# house=[]
# for i in range(n):
#     house.append(int(sys.stdin.readline()))

# house.sort()

# start=house[1]-house[0]
# end=house[-1]-house[0]

# while start<=end:
#     mid = (start+end) //2


import sys
h,m = map(int,sys.stdin.readline().split())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if str(m) in str(i).zfill(2)+str(j).zfill(2)+str(k).zfill(2):
                count+=1
print(count)




# 5 3
# 1
# 2
# 8
# 4
# 9           # 3  1  4  8