# 용액
# 산성용액/알칼리성 용액 : 각 용액의 특성을 나타내는 하나의 정수
# 산성 : 1 ~ 1,000,000,000
# 알칼리성 : -1 ~ -1,000,000,000
# 혼합 용액의 특성값 : 혼합에 사용된 각 용액 특성값의 합
# 같은 양의 두 용액 혼합 -> 특성값이 0에 가까운 용액
# 산성용액, 알칼리성 용액 오름차순 정렬 -> 서로 다른 용액을 혼합하여 특성값이 0에 가까운 용액

# 입력 : 전체 용액의 개수 n(2~100,000)
# 용액의 특성값 : 오름차순 (산성만 or 알칼리성만도 가능)
# 출력 : 첫째줄에 특성값이 0에 가까운 용액을 만들어내는 두 용액의 특성값을 오름차순으로 출력
    # 여러개 이면 아무거나 출력

import sys
# from bisect import bisect_left,bisect_right

n = int(sys.stdin.readline())
liquid = list(map(int,sys.stdin.readline().split()))

# 산성 용액만
if liquid[0]>0:
    print(liquid[0],liquid[1]) 
# 염기성 용액만
elif liquid[-1]<0:
    print(liquid[-2],liquid[-1])
# 산성, 염기성 섞였을 경우
# 버전 1 - bisect 함수 사용
# else:
#     minValue = (0,0)
#     minSum = 1000000000
#     idx = bisect_left(liquid,0)
#     if idx<len(liquid)-1 and abs(liquid[idx]+liquid[idx+1])<minSum:
#         minSum = abs(liquid[idx]+liquid[idx+1])
#         minValue = (liquid[idx],liquid[idx+1])
#     if idx>=2 and abs(liquid[idx-2]+liquid[idx-1])<minSum:
#         minSum = abs(liquid[idx-2]+liquid[idx-1])
#         minValue = (liquid[idx-2],liquid[idx-1])
#     while True:
#         i = liquid.pop()
#         if i < 0:
#             break
#         idx = bisect_left(liquid,-i)
#         if idx < len(liquid) and abs(liquid[idx]+i) < minSum:
#             minSum = abs(liquid[idx] + i)
#             minValue = (liquid[idx],i)
#         if idx > 0 and abs(liquid[idx-1]+i) < minSum:
#             minSum = abs(liquid[idx-1] + i)
#             minValue = (liquid[idx-1], i)
#     print(minValue[0], minValue[1])
# 버전2 - 이진탐색 함수
else:
    res1, res2 = 0,0
    minSum = 1000000000
    left = 0
    right = n-1
    while left < right:
        mix = liquid[left] + liquid[right]

        if abs(mix) < minSum:
            res1, res2 = liquid[left], liquid[right]
            minSum = abs(mix)

        if mix == 0:
            break
        elif mix < 0:
            left += 1
        elif mix > 0:
            right -= 1
        
    print(res1,res2)


# 5
# -99 -2 -1 4 98          # -99 98

# 4
# -100 -2 -1 103          # -2 -1