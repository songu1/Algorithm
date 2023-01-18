# 각 자리가 숫자(0~9)로만 이루어진 문자열 S
# 왼쪽->오른쪽으로 하나씩 모든 숫자를 확인
# 숫자 사이에 X 혹은 +를 넣어 만들어질 수 있는 가장 큰 수
# 모든 연산은 왼쪽부터 순서대로

#첫째 줄 여러개의 숫자로 구성된 하나의 문자열 S (1<= S길이 <=20)

s=list(input())
result=0

for num in s:
    num=int(num)
    if num in (0,1) or result in (0,1):
        result+=num
    else:
        result*=num

print(result)