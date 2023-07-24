# 알바생 강호
# 8시가 될 때까지 손님 문앞에 줄 / 8시 되는 순간 입구에서 커피받음
# 입구에 들어갈때 팁 : 원래주려고 생각했던 돈 - (받은등수-1)
    # 값이 음수라면 받을 수 없음
# 스타벅스 앞에 있는 사람 수 n, 각 사람이 주려고 생각하는 팁 -> 손님 순서를 적절히 바꿨을 때 강호가 받을 수 있는 팁의 최댓값

# 입력 : 스타박스 앞 사람의 수 n (1~100,000)
# 각 사람이 주려고하는 팁(1~100,000)
# 출력 : 강호가 받을 수 있는 팁의 최댓값

import sys

n = int(sys.stdin.readline())
customer = []
for _ in range(n):
    customer.append(int(sys.stdin.readline()))
customer.sort(reverse=True)

result = 0
if customer[-1] >= n-1:
    result = sum(customer) - int(n*(n-1)/2)
else:
    for i in range(n):
        if customer[i] > i:
            result += customer[i] - i

print(result)


# 4
# 3
# 3
# 3
# 3       # 6

# 3
# 3
# 2
# 3       # 5

# 5
# 7
# 8
# 6
# 9
# 10      # 30

# 5
# 1
# 1
# 1
# 1
# 2       # 2

# 3
# 1
# 2
# 3       # 4
