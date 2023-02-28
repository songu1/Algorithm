# 현주 : n명의 인원이 참여하는 프로그래밍 스터디 그룹장
# 대회 3개 개최, 모든 구성원이 각 대회를 참여 (0~1000의 점수, 동점 가능)
# 각 대회별 등수 및 최종 등수 (점수가 높은 순으로 1~n등)
    # 동점일 경우 가능한 높은 등수를 부여
    # 각 사람마다 "나보다 점수가 큰 사람"의 수를 세어 1을 더한 것이 자신의 등수가 됨
    # 대회별 등수는 각 대회에서 얻은 점수를 기준으로, 최종 등수는 3대회의 점수의 합
# 각 참가자의 대회별 등수 및 최종 등수를 출력하는 프로그램
# 입력 : 참가자의 수 n(3~10만)
# 각 대회의 결과를 나타내는 n개의 정수 (i번째 정수, 그 대회에서 i번째 사람이 얻은 점수)
# 출력 : 3개의 줄 각 참가자의 대회별 등수 (각 줄 : 해당 대회의 0, 1, 2, ... 번째 참가자의 등수)
# 마지막 줄에 각 참가자의 최종 등수

import sys

n=int(sys.stdin.readline())
compete=[]      # input 리스트
sorted_list=[]  # 정렬할 리스트
sums=[0]*n      # 합을 계산할 리스트
sorted_slist=[0]*n  # 계산한 합을 정렬한 리스트
for i in range(3):
    # 입력
    instr=sys.stdin.readline()
    compete=list(map(int,instr.split()))
    sorted_list=list(map(int,instr.split()))
    sorted_list.sort(reverse=True)

    # 개별 순위위
    dic={}
    index=1
    for sl in sorted_list:
        if sl not in dic:
            dic[sl] = index
        index += 1
    for j in range(n):
        print(dic[compete[j]], end=" ")
        sums[j] += compete[j]
        sorted_slist[j] += compete[j]
    print()

# 최종 순위
sorted_slist.sort(reverse=True)
dic={}
index=1
for ssl in sorted_slist:
    if ssl not in dic:
        dic[ssl] = index
    index += 1
for j in range(n):
    print(dic[sums[j]], end=" ")
