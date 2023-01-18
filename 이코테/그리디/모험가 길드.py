# 모험가 N명의 공포도 측정
# 공포도 높을 수록 위험상황 대처능력 저하
# 공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹에 참여해야함
# 최대 몇개의 모험가 그룹을 만들 수 있는지(여행을 떠날 수 있는 그룹 수의 최댓값)
# 모든 모험가를 그룹에 넣을 필요X(마을에 남는 사람)

# 첫째줄 : 모험가의 수 N (1<=N<=100,000)
# 둘째줄 : 모험가의 공포도 값 N 이하의 자연수(공백 구분)

N=int(input())
fear=list(map(int,input().split()))
fear.sort()
ftype=list(set(fear))

group=0
n=0

for mem in ftype:
    n+=fear.count(mem)
    group+=n//mem
    if n%mem==0:
        n=0
    else:
        n=n%mem

print(group)


# 강의 풀이 - 오름차순 정렬 후 하나씩 차례대로 그룹에 넣어 보내기 (심플하게 생각하기!)
# n=int(input())
# data=list(map(int,input.split()))
# data.sort()

# result=0    # 총 그룹의 수
# count=0     # 현재 그룹에 포함된 모험가의 수

# for i in data:
#     count+=1        # 현재 그룹에 해당 모험가 포함시킴
#     if count >= i:      # 현재 그룹 모험가수가 현재 공포도 이상 -> 그룹결성
#         result+=1       # 총 그룹의 수 증가
#         count=0         # 현재 그룹 모험가수 초기화
# print(result)