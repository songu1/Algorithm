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
- 2차원 리스트 최대, 최소값 : 최대값, 최소값이 제대로 안나오는 경우가 있음 -> 비추
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
- 사전은 매우 느림(일반 리스트 사용하는 것이 더 빠름)
- dict가 list보다 빠른 경우
    - 리스트에 원소들을 순차적으로 넣고, 탐색할 때에도 순차적으로 탐색해서 찾는 경우에 비해 dict에서 한 번에 접근하는 것이 빠르다
    - list와 dict에서 동일하게 한 번에 같은 리스트에 접근할 수 있다면 list 쪽이 훨씬 빠릅니다.
- dict의 장점
    - 값의 범위가 매우 크더라도 해싱만 되면 데이터를 빠르게 삽입/삭제할 수 있다
    - 들어갈 수 있는 값이 적다면 안쓰는것이 나음
        - 값의 수만큼 리스트로 만들고 체크하기

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

### (4) 숫자로 이루어진 문자열 빈자리 0으로 채우기
- zfill(자릿수)
```python
a="3"
print(a.zfill(3))       # 003
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
### 완전 일치
- ==, !=
```python
print('abc'=='abc')
print('abc'!='xyz')
```

### 부분 일치
- in, not in
```python
'bbb' in 'aaa-bbb-ccc'
'xxx' not in 'aaa-bbb-ccc'
```

### 전방 일치
- startswith()
```python
str.'aaa-bbb-ccc'
str.startswith('aaa')

print(str.startswith(('aaa', 'bbb', 'ccc')))
# True

print(str.startswith(('xxx', 'yyy', 'zzz')))
# False
```

### 후방 일치
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

# 리스트 내 튜플, 리스트 및 사전 정렬

## 1. 리스트안의 튜플, 2차원리스트 정렬
### (1) n번째 원소로 오름차순 정렬
- sort(key=lambda x:x[n])
```python
# 첫번째 원소로 오름차순 정렬
v=[(3,4),(2,2),(3,3),(1,2),(1,-1)]
v2=[[3,4],[2,2],[3,3],[1,2],[1,-1]]

v.sort(key=lambda x:x[0])
v2.sort(key=lambda x:x[0])
print(v)    # [(1,2),(1,-1),(2,2),(3,4),(3,3)]
```

### (2) n번째 원소로 내림차순 정렬
- sort(key=lambda x:-x[n])
- sort(key=lambda x:x[n],reverse=True)
```python
# 첫번째 원소로 내림차순 정렬
v=[(3,4),(2,2),(3,3),(1,2),(1,-1)]
v2=[[3,4],[2,2],[3,3],[1,2],[1,-1]]

v.sort(key=lambda x:-x[0])
v.sort(key=lambda x:x[0],reverse=True)
v2.sort(key=lambda x:-x[0])
v2.sort(key=lambda x:x[0],reverse=True)
print(v)    # [(3,4),(3,3),(2,2),(1,2),(1,-1)]
```

### (3) 첫번재 원소로 오름차순/내림차순, 두번째 원소로 오름차순
- 첫번째 원소 오름차순
    - sort(key=lambda x:(x[0],x[1]))
- 첫번째 원소 내림차순
    - sort(key=lambda x:(-x[0],x[1]))

## 2. 사전 정렬
- sorted()를 이용하여 정렬
### (1) Key를 기준으로 오름차순 정렬
- sorted의 인자로 dict.items()를 전달하면 오름차순으로 정렬
```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
sorted_dict=sorted(my_dict.items())
```

### (2) Key를 기준으로 내림차순 정렬
- sorted()에 reverse=True를 인자로 전달
- lambda가 인자로 전달됨
```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
sorted_dict=sorted(my_dict.items(), key=lambda item:item[0], reverse=True)
sorted_dict2=sorted(my_dict.items(), key=lambda item:-item[0])
```

### (3) Value를 기준으로 오름차순 정렬
- sorted()를 사용하여 Value를 기준으로 정렬
- lambda가 전달, item[1]은 dict의 value
```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
sorted_dict = sorted(my_dict.items(), key=lambda item:item[1])
```

### (3) Value를 기준으로 내림차순 정렬
- sorted()에 인자로 reverse=True 전달
```python
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}
sorted_dict=sorted(my_dict.items(), key=lambda item:item[1], reverse=True)
sorted_dict2=sorted(my_dict.items(), key=lambda item:-item[1])
```

# 리스트 복사
- 단순 '='으로는 주소값이 복사됨
### (1) 슬라이싱
- 리스트가 다른 오브젝트를 포함할 때 오브젝트는 얕은 복사가 됨
- 가장 빠름
```python
list1=[1,2,3,4]
list2=list1[:]
```
### (2) list()함수
```python
list1=[1,2,3,4]
list2=list(list1)
```
### (3) copy() 메소드
- 리스트가 다른 오브젝트를 포함할 때 오브젝트는 얕은 복사가 됨
```python
list1=[1,2,3,4]
list2=list1.copy()
```
### (4) 리스트 연산
```python
list1=[1,2,3,4]
list2=[]+list1
```
### (5) 깊은 복사
- 가장 느림
```python
import copy
list1=[1,2,3,4]
list2=copy.deepcopy(list1)
```
### (6) 배열과 반복문을 이용

# 전역 변수

## 1. 전역 변수 사용
- 일반적으로 프로그램에 혼란을 주기 때문에 사용을 권장하지 않음
- 더 쉽게 가능한 경우에만 사용하기

### (1) 선언
- 변수명 앞에 global 붙이기
- 함수 안과 밖 모두 가능
    - 함수 밖에서 선언 시 함수에서 사용하려면 global명시해줘야함

1. 함수 안에서 global로 전역변수 선언
```python
def func():
    global a
    a=3
    return a
print(func())
```

2. 함수 밖에서 전역변수 선언
```python
global a
a=1
def func():
    global a
    a=3
    return a
```

# zip
## 1. zip
### (1) 기본 문법
- 여러개의 순회 가능한 객체를 인자로 받고 각 객체가 담고있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자를 반환
```python
numbers=[1,2,3]
letters=["A","B","C"]
for pair in zip(numbers,letters):
    print(pair)
# (1, 'A')
# (2, 'B')
# (3, 'C')
```
- zip 처리한 것 출력 시
```python
numbers=[1,2,3]
letters=["A","B","C"]
zip_list=zip(numbers,letters)
print(list(zip_list))
```
### (2) 병렬처리
- 가변인자를 받으므로 2개 이상의 인자를 넘겨서 병렬처리 가능
```python
for number, upper, lower in zip("12345","ABCDE","abcde"):
    print(number,upper,lower)
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e
```
### (3) 사전변환
- dict()함수에 키와 값으로 이루어진 튜플을 넘기면 사전이 생성됨
```python
keys = [1, 2, 3]
values = ["A", "B", "C"]
dict(zip(keys,values))
# {1: 'A', 2: 'B', 3: 'C'}
dict(zip(["year", "month", "date"], [2001, 1, 31]))
# {'year': 2001, 'month': 1, 'date': 31}
```
### (4) 주의사항
- zip()함수로 넘기는 인자의 길이가 다를 때는 주의
- 가장 짧은 인자를 기준으로 데이터가 엮이고 나머지는 버려짐
## 2. upzip
### (1) 기본문법
- 엮어놓은 데이터를 다시 해체
```python
# zip
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)
# [(1, 'A'), (2, 'B'), (3, 'C')]

# unzip
numbers,letters = zip(*pairs)
# numbers : (1,2,3)
# letters : ('A','B','C')
```


# 비트마스킹
## 1. 비트연산자
- AND(&) : 대응하는 두 비트가 모두 1 -> 1반환
- OR(|) : 대응하는 두 비트 중 하나라도 1 -> 1반환
- XOR(^) : 대응하는 두 비트가 둘 중 하나만 참일 때 만족 -> 1반환
- NOT(~) : 비트의 값을 반전하여 반환
- 왼쪽 shift(<<) : 왼쪽으로 비트를 옮김 (a * 2^b)
- 오른쪽 shift(>>) : 오른쪽을 비트를 옮김 (a / 2^b)
## 2. 비트마스크
- check = [False]*10
    => check = 0000000000 으로 확인
1. 원소 추가
- A |= (1 << k)
- k번 원소를 집합 A에 추가
    (1) << 으로 k번 비트만 1로 만듦 
    (2) A와 Or 연산으로 원소 추가
2. 원소 삭제
- A &= ~(1 << k)
- k번 원소를 집합 A에서 삭제
    (1) << 으로 k번 비트만 1로 만든 후 NOT하여 k번 비트만 0이 되고 나머지는 1이 되도록 함
    (2) A와 AND 연산을 하여 원소 삭제
3. 원소 토글
- A ^= (1 << k)
- k번 원소가 집합 A에 있으면 삭제 없으면 추가
    (1) << 으로 k번 비트만 1로 만든 후 XOR 연산
4. 원소의 포함 여부 확인
- if A & (1 << k):
- k번 원소가 집합 A에 있는지 확인
    - << 으로 k번 비트만 1로 만든 후 AND 연산
5. 집합 연산
- A | B
- A & B
- A & ~B
- A ^ B
