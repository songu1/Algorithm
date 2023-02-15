# n명의 학생 정보
# 학생정보 - 학생 이름, 성적

# 입력 : 학생의 수 n (1<= n <= 10만)
# n개의 줄에 학생 이름 문자열 a, 학생 성적 정수 b

# 출력 : 학생 이름을 성적이 낮은 순서대로 출력

import sys
n=int(sys.stdin.readline())
student=[]
for i in range(n):
    a,b=list(map(str,sys.stdin.readline().split()))
    b=int(b)
    student.append([a,b])

student.sort(key=lambda x:x[1])
for st in student:
    print(st[0],end=' ')



# 3
# 홍길동 95
# 이순신 77
# 송유정 100      # 이순신 홍길동 송유정