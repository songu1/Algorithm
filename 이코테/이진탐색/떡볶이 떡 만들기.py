# 떡볶이 떡 만들기 - 풀이 참고
# 떡볶이 떡의 길이가 일정하지 않음
# 한봉지안에 들어가는 떡의 총 길이는 절단기로 자르기
# 절단기 높이 h 지정 -> 줄지어진 떡을 한번에 절단(높이가 h보다 긴떡은 잘림)
# 잘린부분을 손님이 가져감(절단기 밖)
    # 16cm의 떡, 10cm의 절단기 -> 손님 6cm, 절단기 안 10cm
# 손님이 요청한 총 길이 m
    # 적어도 m만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값

# 입력 : 떡의 개수 n, 요청한 떡의 길이 m
# 떡의 개별 높이(떡 높이의 총합은 항상 m이상)

# 출력 : 적어도 m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

#알고리즘
# 적절한 높이를 찾을 때까지 이진탐색을 수행하여 h를 반복해서 조정
# 절단기의 높이 0~10억 -> 큰 탐색 범위를 보면 가장 먼저 이진탐색을 떠올려야함


# 풀이1(재귀함수) - m과 같은 값이 없으면 출력X

def binary_search(array, m, start, end):
    if start > end:
        return None
    mid=(start+end) // 2
    # m 계산
    msum=0
    for a in array:
        if a>mid:
            msum+=a-mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if msum<m:
        return binary_search(array,m,start,mid-1)
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    elif msum>m:
        return binary_search(array,m,mid+1,end)
    else:
        return mid
    

import sys

n,m = list(map(int,sys.stdin.readline().split()))
ricecake=list(map(int,sys.stdin.readline().split()))
ricecake.sort()

start=0
end=ricecake[-1]
result0=binary_search(ricecake,m,start,end)
if result0 is None:
    print('값이 존재하지 않습니다')
else:
    print(result0)


# 풀이 2(반복문) - 문제와 맞게 실행됨 : 추천하는 풀이******
start=0
end=max(ricecake)

# 이진탐색 수행
result=0
while(start <= end):
    total=0
    mid=(start+end)//2
    for x in ricecake:
        # 잘랐을 때 떡의 양 계싼
        if x>mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid-1
    else:
        result=mid      # 최대한 덜 잘라쓸 때가 정답이므로 여기에서 result를 기록
        start=mid+1

print(result)

# 4 6
# 19 15 10 17         # 15

# 5 11                # 값이 존재하지 않습니다
# 28 19 24 15 16      # 20