# 잃어버린 괄호
# 양수, +, -, 괄호로 식을 만들고 괄호를 모두 지움
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들기

# 입력 : 0~9, +, - 만으로 이루어진 식이 주어짐
    # 처음과 마지막은 숫자
    # 연속해서 2개의 연산자X
    # 5자리보다 많이 연속되는 숫자는 없음
    # 숫자 0 으로 시작 가능
# 출력 : 정답을 출력

# + 뒤의 숫자는 결과에 영향을 끼치지 않음
# - 뒤의 숫자가 결과에 영향을 끼침 => -를 기준으로 식을 split하고 -뒤의 수들은 괄호로 묶음

import sys

input = list(map(str,sys.stdin.readline().rstrip().split("-")))

# 첫번째 원소 계산
eq = list(map(int,input[0].split("+")))
result = sum(eq)
# 남은 원소 계산
for i in range(1,len(input)):
    eq = list(map(int,input[i].split("+")))
    result -= sum(eq)
print(result)

# 55-50+40        # -35

# 10+20+30+40     # 100

# 00009-00009     # 0