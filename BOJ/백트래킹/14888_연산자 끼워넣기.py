# 연산자 끼워 넣기 - 시간 줄이는 방법
# n개의 수로 이루어진 수열 / 수와 수사이에 끼워넣는 n-1개의 연산자(+,-,*,//)
# 수와 수사이에 연산자를 넣어 수식을 만듦(수의 순서를 바꾸면 안됨)
# 계산 : 연산자 우선순위 무시하고 앞에서부터 진행
# 음수//양수 => -(양수 // 양수)
# n개의수, n-1개의 연산자 => 만들수 있는 식의 결과의 최댓값고 최솟값

# 입력 : 수의 개수 n(2~11)
# 수열
# 합이 n-1인 4개의 정수 : +, - , * , // 의 개수
# 출력 : 만들 수 있는 값의 최댓값
# 값의 최솟값

import sys

n = int(sys.stdin.readline())
ai = list(map(int,sys.stdin.readline().split()))
a,b,c,d = map(int,sys.stdin.readline().split())

maxVal = - int(1e9) -1
minVal = int(1e9) + 1

def backtracking(val,i,a,b,c,d):
    global maxVal,minVal
    if i >= n:
        maxVal = max(maxVal,val)
        minVal = min(minVal,val)
        return
    
    if a:
        backtracking(val + ai[i], i+1, a-1, b, c, d)
    if b:
        backtracking(val - ai[i], i+1, a, b-1, c, d)
    if c:
        backtracking(val * ai[i], i+1, a, b, c-1, d)
    if d:
        backtracking(int(val / ai[i]), i+1, a, b, c, d-1)

backtracking(ai[0],1,a,b,c,d)

print(maxVal)
print(minVal)


# 2
# 5 6
# 0 0 1 0
# #
# 30
# 30

# 3
# 3 4 5
# 1 0 1 0
# #
# 35
# 17

# 6
# 1 2 3 4 5 6
# 2 1 1 1
# #
# 54
# -24