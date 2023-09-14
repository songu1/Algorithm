# 개똥벌레
# 동굴 길이 n미터(짝수), 높이 h미터
# 첫번째 장애물 항상 석순 / 석순-종유석 번갈이 등장
# 개똥벌레는 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴
# 동굴의 크기, 높이, 장애물의 크기 -> 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간 수

# 입력 : n(2~200,000),h(2~500,000)
# n개의 장애물의 크기(1~h)
# 출력 : 개똥벌레가 파괴해야하는 장애물의 최솟값, 그러한 구간의 수

# 1차시도 : 4% 시간초과

# 2차 시도(이분탐색) : 성공 (59648KB, 2936ms)

# import sys

# n,h = map(int,sys.stdin.readline().split())
# obs1, obs2 = [],[]
# maxObs1, maxObs2 = -1, h+1
# for i in range(n//2):
#     obs1.append(int(sys.stdin.readline()))      # 석순
#     obs2.append(h-int(sys.stdin.readline()))      # 종유석

# obs1.sort()
# obs2.sort()

# def binarySearch1(array,target,start,end,pre):
#     if start > end:
#         return pre
#     mid = (start+end) // 2
#     if array[mid] > target:
#         pre = mid
#         return binarySearch1(array,target,start,mid-1,pre)
#     else:
#         return binarySearch1(array,target,mid+1,end,pre)
    
# def binarySearch2(array,target,start,end,pre):
#     if start > end:
#         return pre
#     mid = (start+end) // 2
#     if array[mid] > target:
#         return binarySearch2(array,target,start,mid-1,pre)
#     else:
#         pre = mid
#         return binarySearch2(array,target,mid+1,end,pre)

# countList = [0]*h
# minObs = n+1   
# count = 0
# for i in range(h):
#     # 장애물 수 구하기
#     c1 = binarySearch1(obs1,i,0,n//2-1,-1)
#     c2 = binarySearch2(obs2,i,0,n//2-1,-1)
#     if c1 >= 0:
#         countList[i] += n//2 - c1
#     if c2 >= 0:
#         countList[i] += c2+1
#     # 최소 장애물수 , 높이 수
#     if countList[i] < minObs:
#         minObs = countList[i]
#         count = 1
#     elif countList[i] == minObs:
#         count += 1
    
# # print(countList)
# print(minObs, count)

# 3차 시도(누적합)
import sys
n,h = map(int,sys.stdin.readline().split())

countList = [0]*h
for i in range(n):
    height = int(sys.stdin.readline())
    # 석순
    if i%2==0:
        countList[0] += 1
        countList[height] -= 1
    # 종유석
    else:
        countList[h-height] += 1

minValue = countList[0]
count = 1
for i in range(1,h):
    countList[i] += countList[i-1]
    if countList[i] < minValue:
        minValue = countList[i]
        count = 1
    elif countList[i] == minValue:
        count += 1
print(minValue,count)

# 6 7
# 1
# 5
# 3
# 3
# 5
# 1           # 2 3

# 14 5
# 1
# 3
# 4
# 2
# 2
# 4
# 3
# 4
# 3
# 3
# 3
# 2
# 3
# 3           # 7 2