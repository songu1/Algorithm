# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열
# 모든 알파벳을 오름차순으로 정렬하여 이어 출력 -> 모든 숫자를 더한 값을 출력

# 입력 : 하나의 문자열 S (1 <= S길이 <= 10000)
# 출력 : 요구하는 정답

import sys
string=[]
num=0
s=list(map(str,sys.stdin.readline().rstrip()))

# 0~9 아스키코드 : 48~57

for i in s:
    if 48<=ord(i)<=57:
        num+=int(i)
    else:
        string.append(i)

string.sort()
if num!=0:
    result="".join(string)+str(num)
else:
    result="".join(string)
    
print(result)

# K1KA5CB7                  # ABCKK13
# AJKDLSI412K4JSJ9D         #ADDIJJJKKLSS20