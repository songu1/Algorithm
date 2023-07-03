# 단어 수학 - 힌트 보고 풂!!
# n개의 알파벳 대문자로 이루어짐
# 각 알파벳 대문자를 0~9 중 하나로 바꿔서 n개의 수를 합하는 문제
# 같은 알파벳은 같은 숫자로 바꿔야하며, 여러개의 알파벳이 같은 숫자X
# n개의 단어 -> 그 수의 합을 최대로 만드는 프로그램
# 예시
    # GCF + ACDEB (783 + 98654) = 99437

# 입력 : 단어의 개수 N(1~10)
# N개의 단어가 주어짐 (모든 단어에 포함된 알파벳은 최대 10개, 수의 길이는 8)
# 출력 : 주어진 단어의 합의 최댓값

# 큰 자리수부터 선택하는 문제풀이 X
# 우선순위 결정 후 숫자 순서대로 넣기

import sys

# 입력
n = int(sys.stdin.readline())   # 단어의 개수
words=[]    # 입력 받을 단어 배열
alpha = [0 for _ in range(26)]     # 0 ~ 25 : ord(문자)-65
result = 0
for i in range(n):
    words.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(len(words[i])):
        alpha[ord(words[i][j])-65] += 10**(len(words[i])-j-1)

# main 코드
alpha.sort(reverse=True)
for i in range(10):
    if alpha[i] == 0:
        break
    result += alpha[i]*(9-i)
    
print(result)


# 2
# AAA
# AAA         # 1998

# 2
# GCF
# ACDEB       # 99437

# 10
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J           # 45

# 2
# AB
# BA          # 187

# 2
# GDF
# ACDEB       # 99427