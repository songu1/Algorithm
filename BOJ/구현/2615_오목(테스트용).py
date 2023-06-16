import sys

# 입력
graph=[]
for _ in range(19):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx=[1,1,0,-1]   # 반시계방향
dy=[0,1,1,1]
# 같은 방향으로만 탐색하는 함수(매번 주위 탐색해서 값이 있다면 다시 양수로 바꾸기)
def search(graph,x,y,color,dir,count):
    # 현재 위치 방문 처리
    graph[x][y] = (-1) * color
    count += 1
    # 주위에 다른 값이 있다면 다시 양수 처리
    for i in range(3,-1,-1):    # dir다음부터 반시계방향
        nx=x+dx[dir-i]
        ny=y+dy[dir-i]
        if nx<0 or nx>=19 or ny<0 or ny>=19:
            continue
        # 같은 색 돌을 찾음
        if abs(graph[nx][ny]) == color:
            # 같은 방향
            if i == 0:
                count = search(graph,nx,ny,color,dir,count)
                return count
            # 다른 방향
            else:
                graph[x][y] = color
    return count



# main 코드
count = -1
for j in range(19):
    for i in range(19):
        if graph[i][j] == 1 or graph[i][j] == 2:
            # 처음 방향 찾기
            for k in range(4):
                ni=i+dx[k]
                nj=j+dy[k]
                if ni<0 or ni>=19 or nj<0 or nj>=19:
                    continue
                if graph[ni][nj] == abs(graph[i][j]):
                    count = search(graph,i,j,graph[i][j],k,0)   # graph,x,y,color,dir,count
                    # 임시 출력
                    print(i+1, j+1, count)
                if count == 5:
                    print(abs(graph[i][j]))
                    print(i+1,j+1)
                    break
            if count == 5: break
    if count == 5: break

if count != 5:
    print(0)

for i in range(19):
    print(graph[i])

