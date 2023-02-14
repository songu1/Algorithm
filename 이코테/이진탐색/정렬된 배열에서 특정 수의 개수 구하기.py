# 특정 수의 개수 구하기 -> bisect 라이브러리 사용!!

# n개의 원소를 포함하고 있는 수열이 오름차순 정렬
# 수열에서 x가 등장하는 횟수 계산
# 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정 -> 이진탐색

# 입력 : 수열의 원소수 n, 횟수계산할 x
# n개의 원소가 공백으로 입력

# 출력 : 수열의 원소 중 값이 x인 원소의 개수 출력(없다면 -1 출력)

def count_by_range(array,x):
    return bisect_right(array,x)-bisect_left(array,x)

import sys
from bisect import bisect_left,bisect_right

n,x=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

count=count_by_range(arr,x)
if count==0:
    print(-1)
else:
    print(count)






# 7 2
# 1 1 2 2 2 2 3          # 4