# 학생 n명 국영수 점수 정렬 프로그램
# 1. 국어 점수 감소하는 순서 (내림차순)
# 2. 영어점수 증가하는 순서 (오름차순)
# 3. 수학점수 감소하는 순서(내림차순)
# 4. 이름이 사전수느올 증가하는 순서 (오름차순)

# 입력 : 학생수 n (1~10만명)
# 한주에 하나식 학생이름, 국어, 영어, 수학 점수 (1~100)

# 출력 : n개의 줄에 학생 이름 출력

import sys
n=int(sys.stdin.readline())
student=[]
for i in range(n):
    student.append(list(map(str,sys.stdin.readline().split())))
    for j in range(1,4):
        student[i][j]=int(student[i][j])

student.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for st in student:
    print(st[0],end='\n')


# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan