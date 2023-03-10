# 공유기 설치 : 이진탐색, 파라메트릭 알고리즘 (반복문 사용하기) ** 풀이 참고
# 도현이네 집 n개가 수직선 위(x1,x2,...xn)
# 어디서나 와이파이를 즐기기 위해 집에 공유기 c개 설치
# 한 집에는 공유기 하나, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
# c개의 공유기를 n개의 집에 적당히 설치 -> 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

# 입력 : 집의 개수 n(2~20만개), 공유기의 개수 c(2~n) (n>=c)
# n개의 줄에 집의 좌표를 나타내는 xi가 한줄에 하나씩
# 출력 : 가장 인접한 두 공유기 사이의 최대거리

# 힌트
# 공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

# 알고리즘
# 0번째 집, 마지막 집 선택 (최소2개)
# 0번째 집과 다른 집 사이의 거리로 이진탐색하기
    # 1과의 거리 최소(start), 최대(end) -> start, end 이진탐색
    # mid값에서의 공유기 수 dnum < c -> start,mid-1 이진탐색
    # mid값에서의 공유기 수 dnum >= c -> mid+1, end 이진탐색 (dnum=c 경우 result=mid 저장하기)
        # start와 end가 같아 더이상 탐색할 수 없음
            # 기존에 저장된 result 출력
        # start > end, result값이 존재하지 않음 -> start=end하여 다시 이진탐색 수행


import sys
n,c=map(int,sys.stdin.readline().split())
house=[]
for i in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

start=house[1]-house[0]
end=house[-1]-house[0]
result=0

while start<=end:
    mid = (start+end) //2
    dnum=1
    value=house[0]
    for i in range(1,n):
        if value+mid <= house[i]:
            dnum+=1
            value=house[i]
    if dnum < c:
        end=mid-1
    else:
        result=mid
        start=mid+1
    # start,end 이진탐색에서 결과를 찾을 수 없을 때
    if start>end and result==0:
        start=end

print(result)


# 5 3
# 1
# 2
# 8
# 4
# 9           # 3

# 6 4
# 7
# 5
# 4
# 10
# 8
# 1           # 3

# 9 3
# 8
# 7
# 5
# 6
# 4
# 100
# 3
# 2
# 1           # 7

# 5 4
# 6
# 10
# 13
# 12
# 2           # 3

# 예시 : (5,3) [1,2,4,8,9]
# 1,8 -> "4" -> (1,8) - 2개 (c보다 작음 -> 이진탐색을 줄임)
# 1,3 -> "2" -> (1,4,8) - 3개 (c이상 -> 이진탐색을 늘림) result 저장
# 3,3 -> "3" -> (1,4,8) - 3개 (c이상 -> 이진탐색을 늘림 but 범위끝) result 저장 -> 출력

# 예시 : (6,4) [1,4,5,7,8,10] 
# 3,9 -> "6" -> (1,7) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 3,5 -> "4" -> (1,5,10) -3개 (c보다 작음 -> 이진탐색 줄임)
# 3,3 -> "3" -> (1,4,7,10) - 4개 (c 이상 -> 이진탐색 늘림 but 범위 끝) result 저장 -> 출력

# 예시 : (9,3) [1 2 3 4 5 6 7 8 100]        ans : 7 ( 1 8 100 )
# 1,99 -> "50" -> (1,100) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 1,49 -> "25" -> (1,100) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 1,24 -> "12" -> (1,100) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 1,11 -> "6"  -> (1,7,100) - 3개 (c 이상 -> 이진탐색 늘림) result 저장
# 7,11 -> "9"  -> (1,100) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 7,8  -> "7"  -> (1,8,100) - 3개 (c 이상 -> 이진탐색 늘림) result 저장
# 8,8 -> "8"   -> (1,100) - 2개 (c보다 작음 -> 이진탐색 줄임 but 범위 끝) -> result값 출력

# 예시 : (5,4) [2,6,10,12,13]
# 4,11 -> "7" -> (2,10) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 4,6  -> "5" -> (2,10) - 2개 (c보다 작음 -> 이진탐색 줄임)
# 4,5  -> "4" -> (2,6,10) - 3개 (c보다 작음 -> 이진탐색 줄임)
# 4,3 -> start>end : start=end 대입하여 다시 실행