# 문자열 압축
# 간단한 비손실 압축 방법
# 문자열에서 같은 값이 연속해서 나타나는 것 -> 그 문자의 개수와 반복되는 값으로 표현
# 연속된 같은 문자 -> 갯수+문자 (1은 생략)
# 제일 앞 문자열부터 정해진 길이만큼 잘라야 함 (자를 단위는 문자열 내에서 같음)
# 출력 : 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이
# 예시
    # ababcdcdababcdcd
        # ab/ab/cd/cd/ab/ab/cd/cd -> (2단위:12)2ab2cd2ab2cd
        # ababcdcd/ababcdcd -> (8단위:9)2ababcdcd
    # abcabcdede
        # ab/ca/bc/de/de -> (2단위:9)abcabc2de
        # abc/abc/ded/e -> (3단위:8)2abcdede
    # aabbaccc
        # a/a/b/b/a/c/c/c -> (1단위 : 7) 2a2ba3c
        # aa/bb/ac/cc -> (2단위 :8 ) 2a2bac2c
    # abcabcabcabcdededededede
        # ab/ca/bc/ab/ca/bc/de/de/de/de/de/de -> (2단위:15)abcabcabcabc6de
        # abc/abc/abc/abc/ded/ede/ded/ede -> (3단위:16)4abcdededededede
        # abca/bcab/cabc/dede/dede/dede -> (4단위:17) abcabcabcabc3dede
        # abcabc/abcabc/dedede/dedede ->  / (6단위:14)2abcabc2dedede
    # xababcdcdababcdcd
        # xababcdcdababcdcd -> (압축X : 17)

# 입력 : 압축할 문자열 s
# 출력 : 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이

import sys
s=sys.stdin.readline()
s=s[1:-2]

def solution(s):
    # 기본길이
    slist=[len(s)]
    # 자르기 (1단위 ~ s//1단위까지)
    for i in range(1,len(s)//2+1):  # 자르는 단위
        count=0
        pre=""
        res=""
        for j in range(0,len(s),i): # 자르기
            # 처음 문자일때
            if pre=="":
                pre=s[j:j+i]
                count=1
            # 이전문자와 현재문자가 같을 때
            elif pre==s[j:j+i]:   
                count+=1
            # 이전문자와 현재문자가 다를 때
            else:
                # 이전문자 2개이상 연속
                if count>=2:
                    res = res + str(count) + pre
                # 이전문자 연속X
                else:
                    res= res + pre
                count=1
                pre=s[j:j+i]
        if count>=2:
            res = res + str(count) + pre
        else:
            res= res + pre
        slist.append(len(res))
    answer=min(slist)
    return answer

print(solution(s))






# "aabbaccc"                    # 7 (aabbacc : 1)
# "ababcdcdababcdcd"            # 9 (2ababcdcd : 8)
# "abcabcdede"                  # 8 (2abcdede : 3)
# "abcabcabcabcdededededede"    # 14 (2abcabc2dedede : 6)
# "xababcdcdababcdcd"           # 17 ()
