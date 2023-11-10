# 파일 합치기
# 소설 여러장 각가 다른 파일에 저장 -> 완성 후 각 장이 쓰여진 파일을 합쳐서 1개의 파일로
    # 2개 파일(원래파일, 임시파일) -> 1개의 임시파일
    # 최종적으로 1개의 파일
    # 비용 : 두 파일 크기의 합
# 소설의 각 장들이 수록된 파일 크기 => 최종적으로 한개의 파일을 완성하는데 필요한 최소 비용

# 입력 : 테스트케이스 수 t
# 각 테스트케이스 2줄
    # 소설을 구성하는 장의 수 k(3~500)
    # 1장부터 k장까지 수록한 파일의 크기 (1~10000)
# 출력 : 모든 장을 합치는데 필요한 최소 비용

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    result = 0
    k = int(sys.stdin.readline())
    size = list(map(int,sys.stdin.readline().split()))
    dp = [[0]*k for _ in range(k)]
    # 2장의 합 구하기 (i~i+1 까지의 합)
    for i in range(k-1):
        dp[i][i+1] = size[i]+size[i+1]
    # print(*dp,sep="\n")
    # n+1(3이상)장의 합 구하기 (i~i+n 까지의 합)
    for n in range(2,k):    # n+1는 합을 구하려는 장수 , n는 시작파일 인덱스와 끝파일 인덱스의 차이
        for i in range(k-n):    # i는 시작파일 인덱스
            minDp = 10000000
            for j in range(n):  # j는 
                minDp = min(minDp,dp[i][i+j]+dp[i+j+1][i+n])
            dp[i][i+n] = minDp + sum(size[i:i+n+1])
        # print(*dp,sep="\n")
        # print()
    print(dp[0][-1])

    # for i in range(k-2):    # 3개
    #     dp[i][i+2] = min(dp[i][i+1],dp[i+1][i+2]) + sum(size[i:i+3])        # 0-2 : 0-1+2,0+1-2
    # print(*dp,sep="\n")
    # for i in range(k-3):    # 4개
    #     dp[i][i+3] = min(dp[i][i+2], dp[i][i+1]+dp[i+2][i+3], dp[i+1][i+3]) + sum(size[i:i+4])      # 0-3 : 0-2+3,  
    # print(*dp,sep="\n")



# 2
# 4
# 40 30 30 50
# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
# #
# 300
# 864

# 1
# 4
# 40 30 30 50