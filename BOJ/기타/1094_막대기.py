# 막대기
# 길이가 64cm인 막대 -> xcm인 막대
# 원래 가지고 있던 막대를 더 작은 막대로 자른 다음 풀로 붙여서 만들기
# 막대 자르기
    # 1. 가지고 있는 막대의 길이를 모두 더함
        # 합 > x
            # 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자름
            # 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 >= x 이면 자른 막대 의 절반 중 하나 버림
        # 남아있는 모든 막대를 풀로 붙여서 xcm를 만듦
# x -> 몇개의 막대를 풀로 붙여서 xcm를 만들 수 있는지 구하는 프로그램

# 입력 : x(1~64)
# 출력 : 몇개의 막대를 풀로 붙여서 x cm를 만들수 있는지

import sys

x = int(sys.stdin.readline())

stick = [64]        # 내림차순으로 정렬하기
sSum = 64
if sSum == x:
    print(1)
    
while sSum > x:
    s = stick.pop()
    s //= 2
    sSum -= s
    if sSum == x:
        print(len(stick)+1)
        break
    elif sSum > x:
        stick.append(s)
    else:
        stick += [s,s]
        sSum += s
    stick.sort(reverse=True)





# 23      # 4
# 32      # 1
# 64      # 1
# 48      # 2