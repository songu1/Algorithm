# 스택
# 정수를 저장하는 스택 구현 -> 입력으로 주어지는 명령을 처리
    # push X / pop(정수가 없으면 -1 출력) / size / empty(비면 1, 아니면 0) / top(가장 위 정수, 없으면 -1)
# 입력 : 명령의 수 n(1~10000)
# 명령
# 출력 : 출력 명령시 한줄에 하나씩 출력

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = list(map(str,sys.stdin.readline().split()))
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top
# #
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

# 7
# pop
# top
# push 123
# top
# pop
# top
# pop
# #
# -1
# -1
# 123
# 123
# -1
# -1