# 암호 만들기
# 암호로 동작하는 보안 시스템
    # 서로 다른 l개의 알파벳 소문자
    # 최소 한개의 모음(a,e,i,o,u)와 최소 2개의 자음으로 구성
    # 알파벳 증가하는 순서로 배열됨
# 암호로 사용했을 법한 문자의 종류 c가지 => 가능성 있는 암호를 모두 구하기

# 입력 : l,c(3~15)
# c개의 문자가 공백으로 주어짐(소문자,중복X)
# 출력 : 한줄에 하나씩 사전식으로 가능성 있는 암호를 모두 출력

# 조합 방식
# 문제, 출력방식 똑바로 읽기!! - 요즘따라 실수가 많다

import sys

l,c = map(int,sys.stdin.readline().split())
alphabet = list(map(str,sys.stdin.readline().split()))
alphabet.sort()

# 백트래킹 함수
def backtracking(idx, arr, countC, countV):
    if len(arr) == l:
        # 모음 수가 0개이거나 자음 수가 1개이하일때
        if countV == l or countC >= l-1:
            return
        print(*arr,sep="")
        return
    
    for i in range(idx,c):
        if alphabet[i] in ('a','e','i','o','u'):    # 자음
            backtracking(i+1,arr + [alphabet[i]], countC+1, countV)
        else:   # 모음
            backtracking(i+1,arr + [alphabet[i]], countC, countV+1)

backtracking(0,[],0,0)

# 4 6
# a t c i s w
# #
# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw