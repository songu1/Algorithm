# 신입 사원
# 1차 서류 심사, 2차 면접 시험
# 서류심사 성적, 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자 선발
    # A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류, 면접 성적이 떨어지면 선발 X
# 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원

# 입력 : 테케 수 t(1~20)
# 각 테스트케이스
    # 지원자 숫자 n(1~100000)
    # 각 지원자의 서류심사, 면접 성적의 순위(1~n위, 동석차 없음)
# 출력 : 각 테스트케이스에 대해 회사가 선발할 수 있는 신입사원의 최대 인원수

# 알고리즘
# 풀이 1 : 서류심사 오름차순 정렬, 면접 내림차순 정렬하여 가장 긴 감소하는 수열 방법으로 풀기! (정렬 + dp) => 시간초과(이중for문 무조건 시간 초과) , LIS 알고리즘과는 다름
# 풀이 2 : sort 후 무조건 앞의 rank[i][1] 값보다 뒤의 rank[i][1]값이 작아야함 (모두와 비교해야하므로)
    # 앞의 값보다 크다면 무조건 제외

import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    rank=[]
    for _ in range(n):
        rank.append(list(map(int,sys.stdin.readline().split())))
    rank.sort()
    count = 1
    pre = rank[0][1]
    for i in range(1,n):
        if rank[i][1] < pre:
            count += 1
            pre = rank[i][1]
    print(count)


# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
# #
# 4
# 3