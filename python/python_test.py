# 코딩테스트를 위한 파이썬 문법 실습
# 실행할 부분 제외 주석처리 후 실행하기

# 1. 자료형

# (1) 리스트 초기화
a=list()    # 빈리스트 선언
a=[0]*10    # 모든 값이 0인 1차원 리스트 초기화
print(a)

# (2) 리스트 메서드
# 특정한 값을 갖는 원소 삭제
a=[1,2,3,4,5,5,5,5]
remove_set={3,5}
result=[i for i in a if i not in remove_set]
print(result)

# (3) 튜플
a=(1,2,3,4)
# a[2]=7 #typeerror

# (4) 사전
data=dict()
data['사과']='apple'
data['바나나']='banana'
key_list=data.keys()
print(key_list)
print(data.values())
for key in key_list:
    print(data[key])

# (5) 집합
data=set([1,2,3])
data.update([5,6])
print(data)


# 2. 입출력

# (1) 나누어 입력 받기
a, b = map(int,input().split())
print(a+b)
a,b=map(int,sys.stdin.readline().split())
print(a+b)

data=list(map(int,input().split())) #각 데이터를 공백으로 구분하여 입력
print(data)

# (2) 입출력 가속
import sys
N=int(sys.stdin.readline())     # 빠른 입력(정수형) - \n까지 입력X
print(N)
N=sys.stdin.readline()          # 빠른 입력 - \n까지 입력됨
print(N)
M=sys.stdin.readline().rstrip()       #빠른입력 - \n제외
sys.stdout.write(M)         # write는 string만 가능
print(M)

from sys import stdin, stdout
input=stdin.readline
print=stdout.write      # write는 string만 가능
N=input()
print(N)

# 3. 배열 입출력

# (1) 우아한 배열 입력
# 1번줄 : 줄 수, 2번줄~ : 공백을 기준으로한 배열
MAP=[list(map(int, input().split())) for _ in range(int(input()))]
print(MAP)

# (2) 정수와 배열이 같은 줄에 들어오는 경우
# 한줄에는 수의 개수 n이 주어지고 그 다음에 n개의 수가 주어짐
N, *arr=map(int,input().split())
print(arr)

# (3) 문자열을 한글자씩 배열에 저장
# 문자열을 한글자씩 배열에 저장
N=int(input())
arr=[list(input()) for _ in range(N)]
print(arr)

# (4) 배열을 연결해서 출력1
arr=[1,2,3,4]
print("".join(map(str,arr)))    # join : '구분자'.join(리스트)
print('/'.join(map(str,arr)))

print(*arr)

# 4. 정수
# (1) 최대, 최소
import sys
ans=sys.maxsize
print(ans)

# 5. 진법
# (1) 10진수 -> 2, 8, 16진수 변환
print(bin(42)) # 2진수
print(oct(42)) # 8진수
print(hex(42)) # 16진수
# (2) 2, 8, 16진수 -> 10진수 변환
print(int('0b101010',2))
print(int('0o52',8))
print(int('0x2a',16))
# (3) 진법 연산
for _ in range(int(input())):
    A, B=map(int,input().split())
    print(bin(A)+bin(B))

# 6. 문자열
# (1) 문자열을 거꾸로
alph="ABCD"
print(alph[::-1])
# (2) 문자열 <-> 아스키코드
print(ord('A'))     # 문자 -> 아스키
print(chr(38))      # 아스키 -> 문자

# 7. 배열

# (1) 배열 초기화
N,M=map(int,input().split())
arr=[[0]*N for _ in range(M)]
print(arr)

# (2) 배열의 원소를 거꾸로
arr=[1,2,3,4,5,4]
arr.reverse()
print(arr)

# (3) 배열 원소 개수
print(arr.count(4))

# (4) 원소 중복 제거
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ] 
alpha=list(set(alpha))
print(alpha)

arr2=[[1,2],[3,4],[1,2]]
print(list(set(map(tuple,arr2))))

# (5) 배열 정렬
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
arr2.sort(key=lambda x:(x[0],x[1]))
print(arr2)

# 8. 기타연산자 : x in 리스트, x not in 문자열