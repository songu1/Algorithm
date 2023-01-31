# 두 배열의 원소 교체
# 두개의 배열 A,B / 두 배열은 N개의 원소로 구성됨, 배열의 원소는 모두 자연수
# 최대 k번 바꿔치기 연산
# 배열 A의 모든 원소의 합이 최대가 되도록
# n,k,배열 A,B => 최대 k번의 바꿔치기 연산 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력

# 입력 : n, k (1 <=ㅜ <= 100,000 / 0 <= k <= n) => O(NlogN)을 보장하는 정렬 알고리즘을 사용해야함
# 배열 A의 원소
# 배열 B의 원소

# 최악의 경우에도 O(NlogN) 보장

import sys

n, k=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break


print(sum(a))



# 5 3
# 1 2 5 4 3
# 5 5 6 6 5         # 26