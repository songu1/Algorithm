# 스타트와 링크
# 총 n명의 사람(짝수), 1~n까지 번호
# n/2씩 스타트팀과 링크팀
# 능력치 Sij : i번 사람과 j번 사람이 같은 팀일 때 팀에 더해지는 능력치
# 팀의 능력치 : 팀에 속한 모든 쌍으 능력치 sij의 합
    # i,j가 같은팀일때 : sij+sji
# 스타트팀과 링크팀의 능력치 차이를 최소화

# 입력 : n(4~20)
# n개의 줄에 n개의 능력치 s
    # [i][j] : Sij / Sii는 항상 0이고 나머지 sij는 1이상 100이하
# 출력 : 스타트팀과 링크팀의 능력치 차이의 최솟값

# 1차시도 : 시간초과
# 순열이 아닌 조합으로 팀원 찾고 다찾으면 능력치 계산

import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))
used = [False]*n

# 백트래킹
def backtracking(idx,num):
    global minDif
    if num == n//2:
        sum = 0
        for i in range(n):
            for j in range(n):
                if used[i] and used[j]:
                    sum += s[i][j]
                elif not used[i] and not used[j]:
                    sum -= s[i][j]
        minDif = min(minDif, abs(sum))
        return

    for i in range(idx,n):
        used[i] = True
        backtracking(i+1,num+1)
        used[i] = False

minDif = int(1e5)
backtracking(0,0)
print(minDif)


# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0             # 0   (1,4) (2,3)

# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0         # 2   (1,3,6) (2,4,5)

# 8
# 0 5 4 5 4 5 4 5
# 4 0 5 1 2 3 4 5
# 9 8 0 1 2 3 1 2
# 9 9 9 0 9 9 9 9
# 1 1 1 1 0 1 1 1
# 8 7 6 5 4 0 3 2
# 9 1 9 1 9 1 0 9
# 6 5 4 3 2 1 9 0     # 1   (1,2,4,5) (3,6,7,8)