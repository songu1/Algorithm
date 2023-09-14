# 개똥벌레
# 동굴 길이 n미터(짝수), 높이 h미터
# 첫번째 장애물 항상 석순 / 석순-종유석 번갈이 등장
# 개똥벌레는 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴
# 동굴의 크기, 높이, 장애물의 크기 -> 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간 수

# 입력 : n(2~200,000),h(2~500,000)
# n개의 장애물의 크기(1~h)
# 출력 : 개똥벌레가 파괴해야하는 장애물의 최솟값, 그러한 구간의 수

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