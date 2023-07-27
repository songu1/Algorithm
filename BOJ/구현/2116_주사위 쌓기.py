# 주사위 쌓기
# 주사위 각 면 1~6 / 마주보는 면 숫자합은 다름
# 규칙
    # 주사위 순서대로 쌓기 : 1,2,3,4,...
    # 쌓기 : 붙어있는 주사위들이 접촉하는 면의 숫자가 같아야함
    # 쌓은 후 : 4개의 옆면 중 어느 한면의 숫자합이 최대가 되도록
# 한 옆면의 숫자의 합의 최댓값을 구하는 프로그램


# 입력 : 주사위 개수 n
# 하나씩 주사위 번호 순서대로 주사위 전개도의 수(a,b,c,d,e,f)
# 출력 : 한 옆면의 숫자의 합이 가장 큰 값을 출력

import sys

n = int(sys.stdin.readline())
dices = [[0]*7 for _ in range(n)]   # 각 주사위 숫자의 마주보는 면을 저장하는 배열
for i in range(n):
    a,b,c,d,e,f = map(int,sys.stdin.readline().split())
    dices[i][a] = f
    dices[i][b] = d
    dices[i][c] = e
    dices[i][d] = b
    dices[i][e] = c
    dices[i][f] = a
# print(*dices,sep="\n")

maxSum = 0
for down in range(1,7):
    sum = 0
    for i in range(n):
        up = dices[i][down]
        if up != 6 and down != 6:   # 둘다 6이 아니면 최대값 6
            sum += 6
        elif up != 5 and down != 5: # 둘 중 하나가 6이고, 다른 하나가 5가 아니면 최대값 5
            sum += 5
        else:                       # 위아래면이 5,6이라면 최대값 4
            sum += 4
        down = up
    maxSum = max(maxSum, sum)

print(maxSum)



# 5
# 2 3 1 6 5 4
# 3 1 2 4 6 5
# 5 6 4 1 3 2
# 1 3 6 2 4 5
# 4 1 6 5 2 3     # 29