# 코딩테스트를 위한 파이썬 문법
### index.py

# 1. 자료형

### (1) 리스트 초기화

```python
a=list()    # 빈리스트 선언
a=[0]*10    # 모든 값이 0인 1차원 리스트 초기화
print(a)
```

### (2) 리스트 메서드

- append, sort, reverse, insert, count, remove
- 특정한 값을 갖는 원소 삭제
    
    ```python
    a=[1,2,3,4,5,5,5,5]
    remove_set={3,5}
    result=[i for i in a if i not in remove_set]
    print(result)
    ```
- 2차원 리스트 최대, 최소값
```python
box=[[1,2,3],[2,3,4],[3,4,5]]
result=max(map(max,box))
result2=min(map(min,box))
```
    

### (3) 튜플

- `a=(1,2,3,4)`
- `~~a[2]=7~~`: type error

### (4) 사전

```python
data=dict()
data['사과']='apple'
data['바나나']='banana'
key_list=data.keys()
print(key_list)
print(data.values())
for key in key_list:
    print(data[key])
```

### (5) 집합 : add, update, remove

```python
data=set([1,2,3])
data.update([5,6])
print(data)
```

# 2. 입출력 ⭐

### (1) 나누어 입력받기 ⭐

```python
a, b = map(int,input().split())

data=list(map(int,input().split())) #각 데이터를 공백으로 구분하여 입력
```

### (2) 입출력 가속 ⭐

```python
import sys
N=int(sys.stdin.readline())     # 빠른 입력(정수형) - \n까지 입력X
print(N)
N=sys.stdin.readline()          # 빠른 입력 - \n까지 입력됨
print(N)
M=sys.stdin.readline().rstrip()       #빠른입력 - \n제외
sys.stdout.write(M)         # write는 string만 가능
print(M)

# 나누어 입력(가속) 받기
a, b =map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split())) # 각 데이터를 공백을 기준으로 나누어 리스트에 입력
data=list(map(int,sys.stdin.readline().rstrip())) #각 테이터를 하나하나씩 리스트에 입력

from sys import stdin, stdout
input=stdin.readline
print=stdout.write      # write는 string만 가능
N=input()
print(N)
```

# 3. 배열 입출력

### (1) 우아한 배열 출력⭐

- 1번줄 : 줄 수
- 2번줄~ : 공백을 기준으로 한 배열

```python
MAP=[list(map(int, input().split())) for _ in range(int(input()))]
print(MAP)

# 배열 선언
n=3
graph=[[] for _ in range(n+1)]
```

### (2) 정수와 배열이 같은 줄에 들어오는 경우⭐

- 한 줄 : 수의 개수 n
- 그 다음 줄 : n개의 수 가 주어짐

```python
N, *arr=map(int,input().split())
print(arr)
```

### (3) 문자열 한글자씩 배열에 저장⭐무

- 문자열을 한글자씩 배열에 저장

```python
N=int(input())
arr=[list(input()) for _ in range(N)]
print(arr)
```
```python
import sys
n=int(sys.stdin.readline())
num=list(sys.stdin.readline().rstrip())
```

### (4) 배열을 연결해서 출력

```python
arr=[1,2,3,4]
print("".join(map(str,arr)))    # join : '구분자'.join(리스트)
print('/'.join(map(str,arr)))

print(*arr)
```

### (5)  임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
```python
import sys
data = list(map(int,sys.stdin.readline().split()))
```

# 4. 정수

### (1) 최대 최소

```python
import sys
ans=sys.maxsize
print(ans)
```

# 5. 진법

### (1) 10진수 → 2, 8, 16진수 변환

```python
print(bin(42)) # 2진수
print(oct(42)) # 8진수
print(hex(42)) # 16진수
```

### (2) 2,8,16진수 → 10진수 변환

```python
print(int('0b101010',2))
print(int('0o52',8))
print(int('0x2a',16))
```

### (3) 진법 연산

```python
for _ in range(int(input())):
    A, B=map(int,input().split())
    print(bin(A)+bin(B))
```

# 6. 문자열

### (1) 문자열을 거꾸로

```python
alph="ABCD"
print(alph[::-1])
```

### (2) 문자열 ↔ 아스키코드

```python
print(ord('A'))     # 문자 -> 아스키
print(chr(38))      # 아스키 -> 문자
```

### (3) 문자열에서 알파벳인 경우 뽑기
- isalpha() 사용하기!!
- 공백이 있거나 숫자와 혼용되면 False를 출력
```python
Ex1 = 'A'
print(Ex1.isalpha())    # True

Ex2 = 'ABC'
print(Ex2.isalpha())    # True
  
Ex3 = "앱피아"
print(Ex3.isalpha())    # True
  
Ex4 = "Hello Appia"
print(Ex4.isalpha())    # False
  
Ex5 = "100Appia"
print(Ex5.isalpha())    # False
```

# 7. 배열

### (1) 배열 초기화

```python
N,M=map(int,input().split())
arr=[[0]*N for _ in range(M)]
print(arr)
```

### (2) 배열의 원소를 거꾸로

```python
arr=[1,2,3,4,5,4]
arr.reverse()
print(arr)
```

### (3) 배열 원소 개수

```python
print(arr.count(4))
```

### (4) 원소 중복 제거

```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ] 
alpha=list(set(alpha))
print(alpha)

arr2=[[1,2],[3,4],[1,2]]
print(list(set(map(tuple,arr2))))
```

### (5) 배열 정렬

```python
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
arr2.sort(key=lambda x:(x[0],x[1]))
print(arr2)
```

# 8. 기타연산자

- x in 리스트
- x not in 문자열

# 9. 형변환 ⭐

### (1) 정수를 리스트로 ⭐

```python
res = [int(x) for x in str(num)]
```

# 10. 문자열 <-> 리스트 ⭐

### (1) join
'구분자'.join(리스트)

```python
a=['a','b','c']
result="".join
```

### (2) split
```python
s="a b c d e f"
r=s.split()
```
문자열.split('구분자',분할횟수)
구분자 : seq=' '

# for문

### (1) for문 변수 여러개 사용
```python
for i,j in zip(a,b):
    ...
```

# 파이썬 예외처리 -> 수정하기!!

```python
try:
    ...
except IndexError:
    ...
```


# 파이썬 문자열 비교
## 완전 일치
- ==, !=
```python
print('abc'=='abc')
print('abc'!='xyz')
```

## 부분 일치
- in, not in
```python
'bbb' in 'aaa-bbb-ccc'
'xxx' not in 'aaa-bbb-ccc'
```

## 전방 일치
- startswith()
```python
str.'aaa-bbb-ccc'
str.startswith('aaa')

print(str.startswith(('aaa', 'bbb', 'ccc')))
# True

print(str.startswith(('xxx', 'yyy', 'zzz')))
# False
```

## 후방 일치
- endswith()
```python
str = 'aaa-bbb-ccc'

print(str.endswith('ccc'))

print(str.endswith(('aaa', 'bbb', 'ccc')))
# True
```

# 경우의 수 - itertools 라이브러리
- from itertools import *

## 1. 순열(Permutation) - 순서O
```python
dataset = ['A', 'B', 'C']

printList = list(permutations(dataset,2))
print(printList)
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

printList = list(permutations(dataset, 3))
print(printList)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

## 2. 조합(Combination) - 순서X
```python
dataset = ['A', 'B', 'C']
printList=list(combinations(dataset,2))
print(printList)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

## 3. 중복 순열(Permutation with repetition) - 순서O, 중복O
```python
dataset = ['A', 'B', 'C']
printList=list(product(dataset,repeat=2))
print(printList)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

## 4. 중복 조합(Combination with repetition) - 순서X, 중복O
```python
dataset = ['A', 'B', 'C']

printList = list(combinations_with_replacement(dataset, 2))
print(printList)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```