# 파도반 수열
# 첫 삼각형 : 정삼각형으로 변의 길이 1
# 나선에서 가장 긴 변의 길이 k일 때 변의 길이가 k인 정삼각형을 추가
# p(n)은 나선에 있는 정삼각형의 변의 길이
    # 1 1 1 2 2 3 4 5 7 9

# 입력 : 테스트케이스 수 T
# 각 테스트케이스 1줄 n(1~100)
# 출력 : 각 테스트케이스마다 p(n)을 출력

import sys
t=int(sys.stdin.readline())
tc=[]
for i in range(t):
    tc.append(int(sys.stdin.readline()))
print(tc)

for i in range(t):
    d=[0]*(tc[i]+1)
    d[1]=1
    if tc[i]>=2:
        d[2]=1
    if tc[i]>=3:
        d[3]=1
    if tc[i]>=4:
        d[4]=2
    for j in range(5,tc[i]+1):
        d[j]=d[j-1]+d[j-5]
    print(d[tc[i]])
    



# 2
# 6
# 12

# 3
# 16