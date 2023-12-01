# 바이러스가 숙주의 몸에서 1초당 p배씩 증가
# 바이러스 k마리 -> n초 후 총 몇마리 바이러스
# k,p : 1~10^8 / n:1~10^6

# k,p,n이 매우 크기 때문에 값을 구하는 도중에 %1000000007 해줘야함!
# 입력값의 범위를 확인하고 시간을 생각하기!

import sys

k,p,n = map(int,sys.stdin.readline().split())

for i in range(n):
  k *= p
  k %= 1000000007  


print(k)