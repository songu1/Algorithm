# 어항 정리
# 상어가 가진 어항 n개이 처음에 일렬로 놓여져있음
# 어항 : 물고기 1마리 이상(값 : 물고기 수)
# 어항 정리 :
    # 1) 물고기 수가 가장 적은 어항에 물고기 한마리 넣음 (여러개라면 모두)
    # 2) 어항 쌓기
        # a. 가장 왼쪽 어항을 오른쪽 어항 위에 올려놓기
        # b. 2개 이상 쌓여있는 어항을 공중부양 시켜 그룹을 시계방향 90도 회전
        # c. 회전한 어항 그룹 가장 왼쪽에 있는 어항에 올려놓기
        # b,c를 공중시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥이 있는 어항이 있을 때까지 반복
            # 즉 어항이 무조건 바닥에 붙어있어야함
    # 3) 어항 물고기수 조절
        # a. d = 모든 인접한 두 어항에서 물고기수의 차이 // 5
        # b. d>0 : 물고기 수가 많은 곳 -> 적은곳 물고기 d마리를 보냄 (모두 동시에 발생)
    # 4) 가장 왼쪽, 아래 어항부터 순서대로 바닥에 놓기
    # 5) 공중 부양 작업
        # a. 가운데를 중심으로 왼쪽 n/2개를 180도 회전시켜 오른쪽 n/2위에 놓기
        # b. a 1번 더 반복
    # 6) 3,4번 재수행
# 어항 수 n , 각 어항에 들어있는 물고기수 -> 물고기가 가장 많이 들어있는 어항과 적게 들어있는 어항의 물고기수 차이가 k이하
    # => 어항을 몇번 정리?

# 입력 : n(4~100 4의 배수),k(0~10)
# 어항에 들어있는 물고기수 (1~10000)
# 출력 : 가장 많은 물고기수 - 가장 적은 물고기수 <=k 인 경우 어항 정리 횟수

n,k = map(int,input().split())
bowl = [list(map(int,input().split()))]     # 바닥이 index 0, 위로갈수록 index 커짐
result = 0      # 어항 정리 횟수

# 어항 쌓기 함수
def stackBowl(bowl):
    # 2개 이상 쌓인 어항 쌓기
    row = len(bowl[1])
    fly = []
    for i in range(row-1,-1,-1):        # 2단에 쌓인 어항(오 -> 왼)
        fly.append([bowl[0][i]])
        del bowl[0][i]
        for j in range(1,len(bowl)):    # 높이 (아래 -> 위)
            fly[row-1-i].append(bowl[j].pop())
    # 빈 1차원 리스트 삭제
    for _ in range(len(bowl)-1): bowl.pop()
    bowl += fly

# 물고기수 조절 함수 - 상,좌(배열 기준 하,우)만 탐색
dx = [1,0]
dy = [0,1]
def controlFish(bowl):
    # 조절할 물고기 수 구하기
    diff = [[0]*len(bowl[i]) for i in range(len(bowl))]
    for x in range(len(bowl)):
        for y in range(len(bowl[x])):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(bowl) or ny < 0 or ny >= len(bowl[nx]):
                    continue
                d = abs(bowl[x][y]-bowl[nx][ny]) // 5
                if bowl[x][y] > bowl[nx][ny]:
                    diff[x][y] -= d
                    diff[nx][ny] += d
                elif bowl[x][y] < bowl[nx][ny]:
                    diff[x][y] += d
                    diff[nx][ny] -= d
    # bowl에 적용
    for x in range(len(bowl)):
        for y in range(len(bowl[x])):
            bowl[x][y] += diff[x][y]

# 바닥에 어항 놓기 함수
def putBowl(bowl):
    arr = []
    for j in range(len(bowl[0])):
        for i in range(len(bowl)):
            if len(bowl[i]) > 0:
                arr.append(bowl[i][0])
                del bowl[i][0]
    return [arr]

# 공중부양 함수
def flybowl(bowl):
    new = []
    length = len(bowl[0])
    for i in range(len(bowl)-1,-1,-1):  # 큰 x값부터
        new .append([])
        for _ in range(length//2):
            new[len(bowl)-1-i].insert(0,bowl[i][0])
            del bowl[i][0]
    bowl += new

while True:
    result += 1
    # 물고기 추가
    minF = min(bowl[0])
    for i in range(len(bowl[0])):
        if bowl[0][i] == minF:
            bowl[0][i] += 1
    # 어항 쌓기 - 여러번 반복
    left = bowl[0][0]
    del bowl[0][0]
    bowl.append([left])
    while len(bowl) <= len(bowl[0])-len(bowl[1]):
        stackBowl(bowl)
    # 어항 물고기수 조절
    controlFish(bowl)
    # 어항 바닥에 나열
    bowl = putBowl(bowl)
    # 반틈 공중 부양 작업
    flybowl(bowl)
    flybowl(bowl)
    # 물고기수 조절 & 바닥에 나열 재수행
    controlFish(bowl)
    bowl = putBowl(bowl)
    # 물고기수 차이 k이하 break
    if max(bowl[0])-min(bowl[0]) <= k:
        break

print(result)


# 8 7
# 5 2 3 14 9 2 11 8           # 1

# 8 4
# 5 2 3 14 9 2 11 8           # 2

# 8 3
# 5 2 3 14 9 2 11 8           # 3

# 8 2
# 5 2 3 14 9 2 11 8           # 4

# 8 1
# 5 2 3 14 9 2 11 8           # 5

# 8 0
# 5 2 3 14 9 2 11 8           # 6

# 4 0
# 1 10000 1 10000             # 10

# 16 0
# 1 1 10000 1 2 3 10000 9999 10 9 8 10000 5 4 3 1     # 13