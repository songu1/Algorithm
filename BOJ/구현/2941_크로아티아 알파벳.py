# 크로아티아 알파벳
# 변경된 크로아티아 알파벳 단어 -> 몇개의 크로아티아 알파벳으로 이루어져 있는지 출력
# c= , c- , dz= , d- , lj , nj , s= , z=
# 위 목록에 없는 알파벳은 한글자씩 셈

# 입력 : 단어(알파벳소문자, -, =) (1~100글자)
# 출력 : 몇개의 크로아티아 알파벳으로 이루어져있는지 출력

import sys

words = list(map(str,sys.stdin.readline().rstrip()))
count = 0
i = 0
while i < len(words):
    count += 1
    if i <= len(words) - 3:
        if words[i] == 'd' and words[i+1] == 'z' and words[i+2] == '=':
            i += 3
            continue
    if i <= len(words) - 2:
        if words[i] == 'c' and words[i+1] in ('=','-'):
            i += 2
            continue
        elif words[i] == 'd' and words[i+1] == '-':
            i += 2
            continue
        elif words[i] == 'l' and words[i+1] == 'j':
            i += 2
            continue
        elif words[i] == 'n' and words[i+1] == 'j':
            i += 2
            continue
        elif words[i] == 's' and words[i+1] == '=':
            i += 2
            continue
        elif words[i] == 'z' and words[i+1] == '=':
            i += 2
            continue
    i += 1

print(count)



# ljes=njak       # 6

# ddz=z=          # 3

# nljj            # 3

# c=c=            # 2

# dz=ak           # 3

# d-z=            # 2