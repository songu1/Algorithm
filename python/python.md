# 파이썬 기본

# 1. 자료형&변수

## 숫자형

```python
print(5)
print(3.14)
print(5+3)
print(3*(3+1))
```

## 문자형

```python
print("풍선")
print('나비')
print("ㅋ"*7)
print("ja"*3)
```

## Boolean형

```python
print(5>10)
print(True)
print(not True)
print(not(5>10))
```

## 변수

```python
name="JADE"
age=25
is_adult=age>=20

print("내 이름은"+name+"에요")       #띄어쓰기 포함X
print(" 내 나이는 "+str(age)+"살입니다")    #문자열사이에 boolean/정수형 출력시 str()사용
print(name+"는 어른일까요? "+str(is_adult))

print("내 이름은",name,"이에요)      #띄어쓰기 포함
print("내 나이는",age,"살입니다")    #정수형/boolean형 변수 그대로 사용가능
print(name,"는 어른일까요?",is_adult)
```

+: 정수형/boolean형 문자열 사이 출력시 : str()

, : 정수형/boolean형 문자열 사이 출력시 : ~~str()~~

## 주석

```python
''' 여러 문장
		주석 처리 '''
#한줄 주석 처리
#일괄 주석 처리 : ctrl+/
```

# 2. 연산자

## 연산자

- +, -, *, %
- ** : 제곱
- // : 몫
- / : 소수점까지 출력
- ==, ! =, and(&), or(|)

## 수식

- +=, *=, -=, /=, %=

## 숫자처리함수

- abs(a) : 절댓값
- pow(a,b) : a^b
- max(a,b) : 최대값
- min(a,b) : 최소값
- round(a) : 반올림
- **from math import ***
    - floor(a) : 내림
    - ceil(a) : 올림
    - sqrt(a) : 제곱근

## 랜덤함수

- 실행할때마다 값이 다르게 나옴

```python
from random import*

random()             # 0.0 ~ 1.0 미만의 임의의 값
random()*10          # 0.0 ~ 10.0 미만의 임의의 실수
int(random()*10)     # 0 ~ 10 미만의 임의의 정수
int(random()*10)+1   # 1 ~ 10 이하의 정수(11미만의 정수)
```

- randrange(a,b) : a ~ b-1 이하의 정수
- randint(a,b) : a ~ b 이하의 정수

# 3. 문자열

## 문자열

- ‘ ‘, “ “
- “””   “”” : 줄 바뀔때 문자열

## 슬라이싱

- 필요한 정보만 잘라서 쓰는 것
- jade[a:b] : a ~ b-1번째까지만
- jade[a] : a번째만
- jade[ :b] : 처음부터 b-1까지
- jade[a: ] : a부터 끝까지
- jade[-7: ] : 맨뒤에서 7번째 부터

```python
jade="980416-2345678"
print("성별: "+jade[7])
print("연도: "+jade[0:2])
print("월: "+jade[2:4])
print("일: "+jade[4:6])
print("생년월일: "+jade[:6])
print("뒤 7자리: "+jade[7:])
print("뒤 7자리(뒤부터): "+jade[-7:])
```

## 문자열 처리 함수

- python=”______string______”
- **python.lower()** : 모두 소문자
- **python.upper()** : 모두 대문자
- **python[a].isupper()** : 대문자인지 아닌지
- **len(python)** : 문자열 길이
- **python.replace(”python”,”java”)** : python이라는 글자를 java로 바꿔줌
- **python.index(”n”)** : n이 몇번째 위치?
- **python.index(”n”,index+1)** : index 다음에서 n이 몇번째 위치?
- **python.find(”n”)** : n이 몇번째 위치?
- **python.count(”n”)** : n이 몇번 등장?
- find, index 차이
    - 원하는 값X
        - find : -1 반환
        - index : error

## 문자열 포맷

```python
print("나는 %d살입니다"%20) #정수값
print("나는 %s을 좋아합니다"%"python") #문자열
print("내 성적은 %c입니다"%"A") #문자

print("나는 %s색과 %s색을 좋아해요"%("파란","빨강"))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨강")) #파 빨
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨강")) #빨 파

print("나는 {age}살이며 {color}색을 좋아해요".format(age=20,color="파란")
#순서 바뀌어도 ok

#v3.6 이상
age=20
color="파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #실제 변수에 저장된 값 사용
```

## 탈출문자

- \n : 줄바꿈
- \”, \’ : 문장내에서 “, ‘
- \\ : 문장내에서 \
- \r : 커서를 맨앞으로 이동
- \b : 백스페이스(한글자 삭제)
- \t : 탭

# 4. 리스트

## 리스트

- [ ]

```python
subway=[10,20,30]
subway=["가","나","다"]  #인덱스 0, 1, 2
subway.index("나")  #나의 인덱스값 -> 1
subway.append("마바")   #맨 뒤에 ()안 값 삽입 -> ['가',....,'마바']
subway.insert(1,"사")   #index 1자리에 "사"삽입 -> ['가','사','나',..'마바']
subway.pop()     #리스트 제일 마지막 값 삭제 -> ['가','사','나','다']
subway.count("가")   #'가'가 몇번 나오는지 출력 -> 1번
sorted(subway)      #문자열 정렬
sorted(subway,reverse=True)     #역순으로 문자열 정렬

num_list=[5,2,4,3,1]
num_list.sort() : 오름차순 정렬  ->  [1,2,3,4,5]
num_list.reverse() : 순서 뒤집기   ->[5,4,3,2,1]
num_list.sort(reverse=True) : 내림차순 정렬
num_list.clear() : 모두 지우기


mix_list=["조세호", 20, True]
num_list.extend(mix_list)   #num_list 뒤에 mix_list를 붙여 확장
														#[5,4,3,2,1,"조세호", 20, True]
```

### 리스트 복사
- 단순 '='으로는 주소값이 복사됨
1. **슬라이싱**
- 리스트가 다른 오브젝트를 포함할 때 오브젝트는 얕은 복사가 됨
- 가장 빠름
```python
list1=[1,2,3,4]
list2=list1[:]
```
2. list()함수
```python
list1=[1,2,3,4]
list2=list(list1)
```
3. copy() 메소드
- 리스트가 다른 오브젝트를 포함할 때 오브젝트는 얕은 복사가 됨
```python
list1=[1,2,3,4]
list2=list1.copy()
```
4. 리스트 연산
```python
list1=[1,2,3,4]
list2.[]+list1
```
5. 깊은 복사
- 가장 느림
```python
import copy
list1=[1,2,3,4]
list2=copy.deepcopy(list1)
```
6. 배열과 반복문을 이용

## 사전

- { 키 : value }
- 키 in 사전(변수 이름) : 키 값이 사전 안에 있는가 → T/F

```python
cabinet={3:"jade", 100:"minseo"}   #키 중복 X
print(cabinet[3])  #jade 가져옴
print(cabinet.get(3))    #jade 가져옴
print(cabinet[5])   #값이 없을 때 오류 출력 후 종료
print(cabinet.get(5))   #none 출력 후 다음 실행
print(cabinet.get(5,"사용가능"))  #"사용가능"출력 후 다음 실행

print(3 in cabinet)

cabinet2={"A-3":"jade", "b-100":"minseo"}   #키값이 다른 자료형도 가능함
print(cabinet2["A-3"])
cabinet2["b-100"]="miyuki"    #원래 키의 값을 다른 값으로 초기화
cabinet2["c-20"]="nao"    #값을 추가
del cabinet2["A-3"]       #키가 지워짐

print(cabinet2.keys())        #키 값만 출력 => dict.keys(['b-100','c-20'])
print(cabinet2.values())     #value만 출력 => dict.values(['miyuki','nao'])
print(cabinet2.items())      #key,value 동시 출력 => dict.items([('b-100','miyuki'), ('c-20','nao')])
cabinet2.clear()             #모든 값 삭제
```

## 튜플

- ( )
- 값을 넣어주는 방법
    - name=”___”, age=__, hobby=”____”
    - (name,age,hobby)=(”___”, ____, “____”)

```python
menu=("엽떡","닭발")   #메뉴변경 없음
print(menu[0])  #엽떡 출력
#menu.add("연어")   #값 추가 변경은 불가능

#값을 하나하나 넣어주기
name="jade"
age=25
hobby="taking a walk"
print(name, age, hobby)

(name,age,hobby)=("jade", 23, "watching netflix")
print(name, age, hobby)
```

## 세트

- { }    or    set([ ])
- 중복이 안됨
- 순서가 없음

```python
my_set={1,2,3,3,3}
print(my_set)   # {1,2,3}

java={10,20,30}
python=set([20,30,50])

#교집합
print(java&python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#차집합
print(java-python)
print(java.difference(python))

python.add(40)    #값 추가
java.remove(10)   #값 삭제
print(python)
print(java)
```

- 교집합 (java와 python 모두에 해당하는 것)
    - java&python
    - java.intersection(python)
- 합집합 (java에 해당하거나 python에 해당하는 것)
    - java|python
    - java.union(python)
- 차집합 (java에는 해당하지만, python에는 해당하지 않는 것)
    - java-python
    - java.difference(python)

## 자료구조의 변경

```python
menu={10, 20, 30} #세트
menu=list(menu)  #리스트로 변경
menu=set(menu)  #세트로 변경
menu-tuple(menu)  #튜플로 변경
```

# 5. 반복문

## if

if 조건:

command

elif 조건:

command

else 조건:

command

```python
temp=int(input("기온은 어때요?"))
if 30<=temp:
	print("It's too hot. Do not go out")
elif 10<=temp and temp<30 :
	print("It's such a good weather")
elif 0<=temp<10:
	print("Bring your outer")
else
	print("It's too cold. Do not go out")
```

- 조건
    - ___ and/or  ___
    - not ___
- str|str 은 불가능

## for

for 변수이름 in _____ :

command

- _____
    - 리스트 : 리스트 내의 값들이 변수에 순차적으로 하나씩 들어가면서 반복
        - 리스트 안에 숫자, 문자형 다 들어갈 수 있음
    - range(a,b) : a이상 b미만 값들이 순차적으로 들어감
        - ex) range(1,6) : 1,2,3,4,5 값이 들어감

```python
#리스트
for num in [0,1,2,3,4]:
	print("번호 : {0}".format(num))

#range
for waiting_num in range(1,6):
	print("대기번호: {0}".format(waiting_num))
```

## while

while(조건) :

command

```python
index=5
customer="jade"
while index>=1:
	print("{0}, coffee is ready {1} times is left".format(customer,index))
	index-=1
	if index==0:
		print("coffee is abandoned")
```

## continue & break

- continue : 밑의 문장 실행 X, 다음 반복 실행
- break : 반복문 탈출

```python
absent=[2,5]
no_book=[7]

for student in range(1,11)
	if student in absent:
		continue
	elif student in no_book:
		print("today's class is finished. {0}, come to my office".format(student))
		break
	print("{0}, please read the book".format(student))
```

## 한줄 for

```python
#출석번호 1,2,3,4 앞에 100을 붙이기로함
students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students=["jade", "karla", "serena"]
students=[len(i) for i in students]
print(students)

#학생 이른을 대문자로 변환
students=["jade","karla","serena"]
students=[i.upper() for i in students]
print(students)
```

# 6. 함수

## 함수

- 정의
    
    def 함수 이름:
    
    command
    
- 호출
    
    함수 이름()
    

```python
def open_account():
	print("new account is opened")
open_account()
```

## 전달값과 반환값

def 함수이름(매개변수1, 매개변수2, ...):

command

return 반환값

```python
#입금
def deposit(balance,money):
	print("Done. balance is {0}".format(balance+money))
	return balance+money
#출금
def withdraw(balance,money):
	if balance>=money
		print("Done. balance is {0}".format(balance-money))
		return balance-money
	else:
		print("Fail. Balance is {0}".format(balance))
		return balance
#저녁시간 출금 수수료
def withdraw_night(balance,money):
	commission=100
	return commision,balance-money-commission #튜플 형식으로 반환

balance=0
balance=deposit(balance,2000)
balance=withdraw(balance,3000)
balance=withdraw(balance,500)
commission,balance=withdraw_night(balance,500)
```

## 기본값

- 함수선언시

```python
def profile(name,age=17,main_lang="python"):   #age, main_lang은 기본값 설정
	print("이름: {0}\t나이: {1}\t 주사용언어: {2}".format(name,age,main_lang))

profile("jade")   #jade,17,python
```

## 키워드값

- 함수 호출 시

def 함수이름(매개변수1, 매개변수2, ...):

command

함수이름(인자1=__, 인자 3=__, 인자2=___, ...)

```python
def profile(name,age,main_lang):
	print(name,age,main_lang)
profile(name="jade",main_lang="python",age=25) #순서가 달라도 키워드값으로 출력 가능
```

## 가변인자

```python
#*로시작하는 매개변수를 이용
def profile(name,age,*language):    #language에 넣고싶은만큼 넣을 수 있음
	print("name: {0}\tage: {1}\t".format(name,age),end=" ")
	for lang in language:
		print(lang,end=" ") #입력받은 language 끝까지
	print()

profile("jade",25,"python","c","java","js")
```

## 지역변수와 전역변수

- 지역변수 : 함수 내에서
- 전역변수 : 프로그램 내에서 모두
- 전역변수 선언
    - global 변수이름

```python
gun=10

def checkpoint(soldiers):
	global gun       #전역 공간에 있는 gun을 함수안에서 사용하겠다
	#gun=20          #지역변수 : 함수 안에서만 사용가능
	gun=gun-soldiers     
	print("[함수 내]남은 총:{0}".format(gun))

def checkpoint_ret(gun,soldiers):
	gun=gun-soldiers
	print("[함수 내]남은 총: {0}".format(gun))
	return gun

print("전체 총: {0}".format(gun)) #10
checkpoint(2) #8 (전역변수이기때문에 값이 그대로
gun=checkpoint_ret(gun,2) #6
print("남은 총: {0}".format(gun)) #6 (매개변수로 넣어주고 값 반환해서 ok)
```

# 7. 입출력

## 표준입출력

- sep : 구분자 (지정해줄 수 있음)
- end : 문장의 끝부분 지정 (원래는 \n으로 설정됨)
- ljust(n) : 왼쪽 정렬, n개의 공간(칸)을 확보
- rjust(n) : 오른쪽 정렬, n개의 공간(칸)을 확보
- .zfill(n) : n크기만큼의 공간을 확보하고 빈공간은 0으로 채워줌
- input(”입력하시오”) : 표준입력 받음

```python
print("python","java")
print("python"+"java")
print("python","java",sep=", ")
print("python","java","javascript",sep=" vs")
#한줄에 두개의 문장이 출력
print("python","java",sep=", ",end="? ")
print("무엇이 더 재미있을까요?")

import sys
print("python","java",file=sys.stdout)  #표준출력 / sys.stdout : 표준출력장치 모니터
print("python","java",file=sys.stderr)  #표준에러-확인해서 프로그램 코드 실행(필요시 에러처리)

#사전 이용, ljust,rjust - 시험성적
scores={"math":0, "english":50, "coding":100}
for subject, scores in scores.items():  #사전 사용시 items를 해 key와 value를 쌍으로 튜플로 보내줌
	print(subject.ljust(5),str(score).rjust(4),sep=":")

#zfill, 001,002,... - 은행 대기 순번표
for num in range(1,21):
	print("대기번호: "+str(num).zfill(3)) #3크기만큼의 공간을 확보하고 빈공간을 0을 채워줌

#표준입력
answer=input("아무값이나 입력하세요: ")
print(type(answer))  #사용자입력을 받으면 항상 문자열로
print("입력하신 값은 "+answer+"입니다.")

answer=10
print(type(answer))  #정수형
print("입력하신 값은 " +str(answer)+"입니다.")
```

## 다양한 출력포맷

- {0: >10}
    - : 빈자리는 빈공간으로 두기
    - >: 오른쪽 정렬
    - 10: 10자리 공간 확보
    - 부호는 음수일때만
- {0:_>+10}
    - _ : 빈자리는 _로 채우기
    - +: 값이 양수일때는 + 부호, 음수일때는 - 부호 붙이기
    - 오른쪽 정렬, 10자리 공간 확보
- {0:^<+30,}
    - 30자리 확보, 빈자리^로 채우기, 왼쪽정렬, 부호표시, 3자리마다 ,찍기
- {0:f}
    - 소수점 출력(6자리까지)
- {0:.2f}
    - 소수점 2자리까지 출력

```python
#빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500)) #
print("{0: >10}".format(-500)) #부호출력, 양수일 경우 부호 출력X
print("{0: >+10}".format(500)) #양수일땐 +표시,음수 일땐 -표시
print("{0:_<+10}".format(500)) #10자리 공간확보, 빈칸을 _로 채움, 부호 표시

#3자리마다 콤마 찍기
print({0:,}.format(1000000000)) #3자리마다 콤마를 찍어줌
print({0:+,}.format(10000000000)) #3자리마다 콤마를 찍고 부호 표시
print({0:^<+30,}.format(100000000))

#소수점 출력
print("{0:f}".format(5/3)) #소수점 출력(소수점 6자리까지)
print("{0:.2f}".format(5/3)) #소수점 특정자리수까지만 표시(소수점 3째자리에서 반올림)
```

## 파일입출력

- open(”output.txt”,”w”,encoding=”utf8”)
    - w : 쓰기위한 파일, 이미 존재하는 파일에 사용하면 덮어쓰기됨
    - utf8 : 한글정보 제대로 입력 위해
- open(”output.txt”,”a”,encoding=”utf8”)
    - a: 이미 내용이 존재하는 파일에 이어서 쓰기
- 파일 출력
    - print(”___”,file=f) : 줄바꿈 포함
    - f.write(”___”) : 줄바꿈이 따로 없음 → 명시해줘야함
- open(”score.txt”,”r”,encoding=”utf8”)
    - r : 읽기
- 파일 읽기
    - f.read() : 내용을 읽음
    - f.readline() : 줄별로 읽기, 한 줄 읽고 cursor는 다음줄로 이동(줄바꿈 포함)
    - f.readlines() : 리스트 형태로 읽어서 저장

```python
#파일 받아서 쓰기
score_file=open("score.txt","w",encoding="utf8")
print("수학 : 0",file=score_file)
score_file.write("과학 : 80")
score_file.close()

#파일 읽기
score_file=open("score.txt","r",encoding="utf8")
print(score_file.read()) #전체 내용 읽어옴
print(score_file.readline()) #줄별로 읽기
print(score_file.readline(),end="") #줄바꿈 안하고 싶으면
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
#파일이 몇줄인지 모를때
while True: #무한루프
	line=score_file.readline()
	if not line: #읽은 것이 없을때
		break
	print(line,end="")
#리스트에 값을 넣어 처리하기
lines=score_file.readlines() #list형태로 저장
for line in lines:
	print(line,end="")
score_file.close()
```

## pickle

- 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장
- 파일을 누군가에게 주면 파일을 열어 pickle을 가지고와 코드에서 또 쓸 수 있음
- open(”profile.pickle”,”wb”)
    - wb: write binary
    - encoding 설정할 필요 없음
- pickle.dump(profile,profile_file)
    - profile(사전)에 있는 정보를 profile_file(파일)에 저장
- open(”profile.pickle”,”rb”)
    - rb : read binary
- pickle.load(profile_file)
    - profile_file(파일)에 있는 니용을 그대로 가지고옴

```python
import pickle
profile_file=open("profile.pickle","wb")
profile={"name":"jade", "age":25, "hobby":["drum","kickboxing","coding"]}
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

#파일에서 데이터를 가지고옴
profile_file=open("profile.pickle","rb")
profile2=pickle.load(profile_file) #파일에 있는 내용을 그대로 가지고와 데이터형태로 profile에 저장
profile_file.close()

```

## with

- with 사용시 매번 close 안해줘도 됨
- with open("profile.pickle","rb") as profile_file: / with open(”profile.txt”,”r”) as profile_file:
    - 파일을 열어서 profile_file이라는 변수에 저장
- with open(”profile.txt”,”w”) as profile_file:
    - 파일을 열어 profile_file이라는 변수에 저장

```python
import pickle

with open("profile.pickle","rb") as profile_file: #파일을 열어 변수에 저장
	print(pickle.load(profile_file)) #파일내용불러와 저장

with open("study.txt","w",encoding="utf8") as study_file:
	study_file.write("I'm studying python")

with open("study.txt","r",encoding="utf8") as study_file:
	print(study_file.read())
```

# 8. 클래스
## 클래스

- 실제 게임할때 수십 수백개의 유닛이 필요함 → 클래스

```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1=Unit("마린",40, 5)  # self를 제외한 나머지를 입력해줌
marine2=Unit("마린",40, 5)
tank=Unit("탱크",150,35)
```

## init

- `__init__`  : 생성자
- 객체가 만들어질 때 자동으로 호출되는 부분
- 객체 : 클래스로부터 만들어지는 것 (ex - 마린, 탱크)
- 마린, 탱크 - Unit 클래스의 instance
- 객체 생성될 때 유닛함수에 정의된 개수와 동일하게 self 제외

```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1=Unit("마린",40, 5)  # self를 제외한 나머지를 입력해줌
marine3=Unit("마린",40) #에러
```

## 멤버변수

- self.name, self.hp, self.damage 에서 name, hp, damage : 멤버변수
- 클래스에 대해서 정의된 변수
- 어떤 객체에 추가로 변수를 외부에서 만들어 쓸 수 있음(확장가능)
    - 확장을 한 객체에 대해서만 적용

```python
class Unit:
    def __init__(self, name, hp, damage):
        self.name=name  
        self.hp=hp                          
        self.damage=damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 =Unit("레이스",80,5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#클래스 외부에서 멤버변수 사용

#마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음)
wraith2=Unit("빼앗은 레이스",80,5)
wraith2.clocking= True      #외부에서 변수를 추가로 할당
#레이스1에는 clocking이 없음

if wraith2.clocking==True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking==True:      #클로킹 없음
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
```

