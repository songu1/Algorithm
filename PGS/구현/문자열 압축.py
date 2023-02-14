# 문제를 이해못하겠다!!!

# 문자열에서 같은 값이 연속해서 나타나는 것 -> 그 문자의 개수와 반복되는 값으로 표현
# 연속된 같은 문자 -> 갯수+문자
# 1은 생략
# 제일 앞 문자열부터 정해진 길이만큼 잘라야 함
# 자를 단위는 문자열 내에서 같음
# ex) abcabcdede -> 2abcdede (단위 : 3) 
#                -> abcabc2de (단위 : 2)

# 입력 : 압축할 문자열 s
# 출력 : 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이

import sys
s=sys.stdin.readline()
s=s[1:-2]








# "aabbaccc"                    # 7 (aabbacc : 1)
# "ababcdcdababcdcd"            # 9 (2ababcdcd : 8)
# "abcabcdede"                  # 8 (2abcdede : 3)
# "abcabcabcabcdededededede"    # 14 (2abcabc2dedede : 6)
# "xababcdcdababcdcd"           # 17 ()
