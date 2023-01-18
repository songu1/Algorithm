# 어떠한 수 N이 1이 될 때까지 다음 두과정 중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다
# 2. N에서 K로 나눈다 (N이 K로 나누어 질 때만 가능)

# 첫째줄 N(1<=N<=100,000)과 K가 공백을 기준으로 자연수로 주어짐

N, K=map(int,input().split())

count=0

while N>1:
    rest=N%K
    if rest==0:
        N//=K
        count+=1
    else:
        count += rest
        N-=rest
if N==0:
    count-=1

print(count)