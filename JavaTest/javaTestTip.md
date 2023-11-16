# 자바 코딩테스트 문법 속성 정리
**import java.util.*;**


## [1] 기본 문법
> String : 한 번 만들어지면 문자를 추가하거나 삭제할 수 없는 변경 불가 타입
>
> StringBuilder : 변경 가능한 타입
### (1) String 관련 메소드
- 길이 고정
```java
String str = "abcde";

str.length()    // str의 길이
str.isEmpty()   // str길이가 0이면 true, 아니면 false

str.charAt(2)   // 인덱스로 문자 찾기
str.indexOf("c")    // 문자로 첫번째 인덱스 찾기
str.lastIndexOf("c")    // 문자로 마지막 인덱스 찾기

str.substring(2,4)  // 2~3 위치의 문자열 "cd" 반환
str.substring(3)    // 3부터 끝까지의 문자열 "de" 반환

str.replace('b','k')    // b를 k로 변경(akcde)
str.replaceAll(".","/") // 모든 문자(".")를 "/"로 변경
str.replaceFirst('p','e');  // 여러 문자중 첫번째만 치환(aeple)

str.equals("abcde")     // str과 비교해서 같으면 true, 다르면 false
str.contains("bc")      // str에 bc가 포함되면 true, 아니면 false

str.split(" ")  // 띄어쓰기로 구분된 문자열 str을 분리해서 String[]배열로
str.split()     // 띄어쓰기 없는 문자열 str을 한 문자씩 분리하여 String[] 배열로

str.trim()      // str 앞뒤 공백 제거(문자열 사이 공백은 제거x)

str.toLowerCase()   // 대문자를 모두 소문자로 변경
str.toUpperCase()   // 소문자를 모두 대문자로 변경
// 문자가 대문자인지 소문자인지 확인
char a='a'
Character.isUpperCase(a);
Character.isLowerCase(a);

str.compareTo("abcdd")
// str이 abcdd와 같으면 0
// str이 abcdd보다 사전순으로 앞 -1
// str이 abcdd보다 사전순으로 뒤면 1

Interger.parseInt("300")    // 문자열을 숫자로 변환
Interger.parseString(300)   // 숫자를 문자열로 변환
```

#### StringBuilder 관련 메소드
```java
StringBuilder sb = new StringBuilder();

sb.append("abc")    // 문자열 추가 (abc)
sb.append(2,"kk")   // 2위치에 kk삽입 (abc->abkkc)

sb.delete(0,2)      // 0~1 위치의 문자열 삭제 (abc -> c)
sb.deleteCharAt(2)  // 2 위치의 문자 삭제 (abc -> ab)

sb.setCharAt(0,'h') // 0위치의 문자를 h로 변경 (abc -> hbc)

sb.reverse()    // 문자열 거꾸로 뒤집기 (abc -> cba)

sb.setLength(2)     // 문자열 길이를 2로 줄임
sb.setLength(4)     // 문자열 길이를 4로 늘림(뒤에 공백 추가)
```

#### StringBuffer 클래스
- String은 공간, 시간 낭비가 큼 => StringBuffer 사용
```java
StringBuffer str = new StringBuffer("Java Oracle");
System.out.println("원본 문자열:" + str);
str.delete(4,8);    // 인덱스에 해당하는 부분문자열을 제거
str.deleteCharAt(1);    // 특정 위치의 문자 1개 제거
str.insert(4,"Script");     // 지정된 인덱스 위치에 "Script"를 추가
str.toString();     // 마지막에 해줘야함
```

### (2) Array(배열) 관련 메소드
- 배열 크기가 한정되어있음 => 크기는 불변
- 미리 공간의 갯수(길이)를 정해야함
- 배열 공간 늘리기 : 따로 공간이 큰 배열을 만들고 기존 배열 내용을 복사
```java
// 배열 선언 및 초기화
int[] score = new int[5];   // int 타입의 값 5개가 저장될 빈 공간 생성
score[0] = 10;
score[1] = 20;
score[2] = 30;
score[3] = 40;
score[4] = 50;

// for문으로 배열을 순차적을 순회하여 값을 생성
int[] number = new int[5];
for(int i = 0; i< score.length; i++)
    number[i] = i*10;

int[] score2 = {10,20,30,40,50};

// 배열 출력
System.out.println(Arrays.toString(score))
System.out.println(Arrays.toString(score2))

// 배열 복사
arr = Arrays.copyOf(scores2,scores2.length);    // scores2배열을 scores2.length 전체 길이 만큼 전체 복사하여 arr에 할당

// 배열 분할
arr = Arrays.copyOfRange(scores2,1,3);  // 배열요소 시작점, 끝점 지정(1,2만 복사하여 반환)

// 배열 정렬(자기 자신 배열을 정렬)
Arrays.sort(score); // 오름차순 정렬
Arrays.sort(score,0,3);     // 배열요소 0,1,2만 정렬
Arrays.sort(score,Collections.reverseOrder())   // 내림차순 정렬(int[]타입 불가능, Integer[] 타입만 가능)
// 2차원 배열 정렬
Arrays.sort(score, (o1,o2) -> {
    return o1[0]-o2[0];    // 첫번째 숫자 기준 오름차순 정렬
});
Arrays.sort(meeting,(o1,o2) -> {
    if(o1[0] == o2[0]){
        return o1[1]-o2[1];
    }
    return o1[0]-o2[0];
});
Arrays.sort(score, Comparator.comparingInt((int[] o) -> o[0]));    // 첫번째 숫자 기준 오름차순
Arrays.sort(score, Comparator.comparingInt((int[] o) -> o[0]).reversed());    // 첫번째 숫자 기준 내림차순

// 정렬 후 특정 값 찾기
Arrays.binarySearch(score,2);

// 배열 비교
Arrays.equals(score, score2);

/* 2차원 배열 */
// 생성 및 초기화
int[][] arr = new int[4][3];
arr[0][1] = 10;
...

int[][] arr2 = {
    {10,20,30},
    {10,20,30},
    {10,20,30},
    {10,20,30}
}
//출력
System.out.println(Arrays.deepToString(arr2));
// 비교
Arrays.deepEquals(arr,arr2);
```

### (3) List 관련 메소드
- List vs Array
    - Array : 배열의 크기가 한정되어있음
    - List : 크기가 정해져있지 않고 동적으로 변함
        - ArrayList, Vector, LinkedList 등 List 인터페이스를 구현한 자료형이 존재
- add, get, size, contains, remove
- ArrayList로 사용
```java
// 선언
List<String> list = new ArrayList<>();

//선언 및 초기화
List<String> list1 = new ArrayList<>(Arrays.asList("apple","banana","grape"));  // 크기 가변
List<String> list2 = Arrays.asList("apple","banana","grape");                   // 크기 불변

list.add("서울")    // list의 가장 뒤에 서울 삽입
list.add(1,"대전")  // 1위치에 대전 삽입
list.addAll(list2)  // list의 뒤에 list2의 모든 값을 삽입
// 빈리스트에 addAll하면 깊은 복사

list.get(0)     // 0 위치의 값 반환(서울)
list.set(0,"대구")  // 0위치의 값을 대구로 변경

list.indexOf("대구")    // 대구의 첫번째 인덱스 반환
list.lastIndexOf("대구")    // 대구의 마지막 인덱스 반환

list.remove(0)      // 0위치의 값 삭제
list.remove("대구") // 첫번째 대구 삭제
list.removeAll(list2)   // list에서 list2에 들어있는 모든 값을 삭제
list.retainAll(list2)   // list에서 list2에 들어있는 값을 제외한 모든 값을 삭제

list.clear()    // 전체 값 삭제
list.isEmpty()  // 길이가 0이면 true, 아니면 false
list.size()     // 길이

list.contains("서울")       // 서울이 list에 있으면 true, 없으면 false
list.containsAll(list2)     // list에 list2의 모든 값이 포함되어있으면 true

list.removeIf(k -> k%2 != 0)    // 람다식으로 홀수를 list에서 모두 제거
```

#### 📚 배열 <-> 리스트 
```java
// 문자열 배열 -> list
String[] temp = {"apple","banana","grape"};
List<String> list = new ArrayList<>(Arrays.asList(temp));

// list -> 문자열 배열
List<String> list = new ArrayList<>();
String[] temp = list.toArray(new String[list.size()]);

// 정수배열 -> list
int[] temp = {1123, 1412, 23, 44, 512132};
List<Integer> list = new ArrayList<>(Arrays.asList(temp));

// list -> 정수 배열
List<Interger> list = new ArrayList<>();
int[] temp = list.stream().mapToInt(i->i).toArray();


/* for문 사용하여 list -> 배열 */
// 배열크기는 list.length크기와 같게 선언되어있어야함
for (int i = 0; i<list.length() ;i++){
    arr[i] = list.get(i);
    arr2[i] = list2.get(i).intValue();
}
```

### (4) Collections 관련 메소드
```java
import java.util.*;

int[] arr = {1123,1413,23,44,512132}
List<Integer> list = new ArrayList<>(Arrays.asList(arr))

Collections.max(list)   // list 원소 중 가장 큰 값 반환
Collections.min(list)   // list 원소 중 가장 작은 값 반환
System.out.println(list)

Collections.sort(list)  // list 오름차순 정렬
Collections.sort(list,Collections.reverseOrder())   // list 내림차순

Collections.reverse(list)   // list 역순 정렬

Collections.frequency(list, 23)     // list내의 23의 개수 반환

// 졍렬된 리스트에서 index 반환
Collections.binarySearch(list,44)
// 최초로 검색된 44의 인덱스 1 반환
// 없으면 44보다 큰 최초의 위치 2를 찾아 -1을 곱하고 1을 빼서 반환 (-3)
```

### (5) Stack
```java
Stack<Integer> stack = new Stack<>();

stack.push(1)   // 값 추가
stack.pop()     // 값 삭제
stack.clear()   // 값 전체 삭제
stack.size()    // 크기 반환
stack.empty()   // 비어있으면 true, 아니면 false
stack.contains(1)   // 1을 포함하면 true, 아니면 false
stack.peek()        // stack top출력, 비어있으면 null 반환
```

### (5) Queue
- offer : 삽입
- poll : 꺼냄
- peek : 보기만
- size, isEmpty
```java
Queue<Integer> queue = new LinkedList<>();

queue.add(1)    // 값 추가
queue.offer(2)  // 값 추가(삽입)
queue.poll()    // 첫번째 값 반환, 비어있으면 null 반환
queue.remove()  // 첫번째 값 제거
queue.clear()   // 값 모두 삭제
queue.peek()    // 첫번째 값 출력(제거X)
```

### Dequeue
- queue랑 동일 + pollFirst, pollLast, get
```java
Deque<E> dp = new ArrayDeque<E>();
```

### (6) PriorityQueue
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();

pq.add(1)       // 값 추가
pq.offer(1)     // 값 추가
pq.poll()       // 첫번째 값 반환, 비어있으면 null 반환
pq.remove()     // 첫 번째 값 제거
pq.clear()      // 값 모두 삭제
pq.peek()       // 첫 번째 값 출력
```

### (7) HashSet
- **Set** : 중복을 허용하지 않는 구조
    - **HashSet** : 순서x, 정렬x
    - **LinkedHashSet** : 삽입된 순서대로 관리
    - **TreeSet** : 이진트리 형태로 데이터를 저장하므로 정렬
- add, contains, equals, isEmpty, size
- Object[] toArray
```java
HashSet<Integer> set = new HashSet<>();

set.add(1)      // 값 추가
set.remove(1)   // 값이 1인 데이터 삭제
set.removeAll(set2)     // set의 데이터 중 set2에 들어있는 데이터를 모두 삭제
set.removeAll(set2)     // set의 데이터 중 set2에 들어있지 않은 데이터를 모두 삭제
set.clear()     // 모든 데이터 삭제
set.size()      // 크기 반환
set.contains(1)     // 값 1이 있으면 true, 없으면 false


/* 값 출력 */
// 방법1 : get 메소드가 없으므로 원소에 접근하려면 iterator 사용
Iterator iter = set.iterator();
while(iter.hasNext())
    System.out.println(iter.next());
// 방법2 : for-each
for (String item: set)
    System.out.println(item);
```

### (8) HashMap
- **HashMap** : <key, value> 쌍. 특정 규칙 없이 출력
- **LinkedHashMap** : <key,value>쌍. 키값이 입력순으로 정렬되어 출력됨
- **TreeMap** : <key,value>쌍. 키값이 알파벳순(오름차순)으로 정렬
- put, get, containsKey, remove, size

```java
// 순서x : hashmap, 들어간 순서 : linkedhashmap, 오름차순 : treemap으로 사용하면 됨
HashMap<Integer, String> map = new HashMap<>();
// HashMap<String, String> map = new HashMap<>();

map.put(1,"사과");
map.put(2,"바나나");
map.put(1,"포도")   // key 1이 이미 존재하면 key1의 value가 포도로 대체

map.remove(1)   // key값으로만 요소 삭제
map.clear()     // 전체 삭제

map.containsKey(1)  // key 값중 1이 있으면 true, 없으면 false
map.containsValue("사과")   // value 중 "사과"가 있으면 true, 없으면 false

// 반복문
for (type var:iterate){
        body-of-loop
    }

/* 값 출력 */
for(Integer i:map.keySet())
    System.out.println(i+map.get(i));   // 1 사과


for (Entry<Integer, String> entry: map.entrySet())
    System.out.println(entry.getKey() + entry.getValue());  // 1 사과
```

### (9) LinkedList
```java
LinkedList list = new LinkedList();
LinkedList num2 = new LinkedList<>();
```
- addFirst, addLast, add
- removeFirst, removeLast, remove, clear
- size, hasNext
- contains


## [2] 입출력
- System.out.println(""), Scanner

    => 시간 소모가 큼
### (1) 자바 입력 클래스
#### BufferedReader
- 정수를 입력받는 함수를 제공하지 않으므로 필요한 경우 직접 변환해야함
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String input = br.readLine();

// 정수로 변환
int a = Integer.parseInt(br.readLine());

// 공백이 있는 입력
String[] inp = br.readLine().split(" ");
```
#### StringTokenizer
- 공백으로 값이 구분되는 경우
```java
StringTokenizer st = new StringTokenizer(br.readLine());

int a = Integer.parseInt(st.nextToken());
int b = Integer.parseInt(st.nextToken());
int c = Integer.parseInt(st.nextToken());
```

### (2) 자바 출력 클래스
- 적은 양의 출력 : System.out.println("")
- 많은 양의 출력 : BufferedWriter

### BufferdWriter
1. bw.write() : 버퍼에 값을 저장
2. flush() or close() : 값을 출력
    - 출력 후 종료 : close()
    - 더 출력한다면 : flush()
- BufferedWriter 사용 후에는 반드시 flush()나 close() 중 하나를 작성해야함
```java
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.write("hello bf!");  // 괄호 안의 값을 출력
bw.newLine();   // 줄 바꿈
bw.flush(); // 버퍼에 남아있는 데이터를 비운 후, 해당 데이터를 출력
bw.close(); // 버퍼에 남아있는 데이터를 비운 후, 해당 데이터를 출력한 후 스트림이 닫힘 -> 해당 스트림 다시 이용 불가능
```

## [3] 팁
### (1) 팁
#### 1) 특정 배열에 값을 넣을 때 중복 없이 넣기
- indexOf는 특정 value가 없으면 -1을 return
```java
// ArrayList를 선언하고 특정 값이 value일 때
List<String> list = new ArrayList<>();
list.add("apple");
list.add("banana");
// String value = "apple";
String value = "grape";

// 배열에 중복없이 값을 넣기
if(list.indexOf(value) < 0)
    list.add(value);
```
#### 2) 특정 정수를 잘라서 사용하고 싶을 때
```java
value = 123
while(value != 0){
    remain = value % 10
    value /= 10;
}
```

#### 3) 배열 특정 값의 index 리턴 받기
1. Arrays.sort() 메소드로 정렬
2. Arrays.binarySearch() 메소드로 항목의 인덱스값 찾기
```java
String[] members = {"aa","bb","cc"}
Arrays.sort(members);
int idx = Arrays.binarySearch(members,"bb");
```

#### 4) 같은 key인경우 value에 리스트로 추가
- hashmap에 key 단위로 value를 arraylist로 담기
```java
public static HashMap<String, ArrayList<String>> joinDic(String[] arr){
    // dic이름의 hashmap을 선언
    HashMap<String,ArrayList<String>> dic = new HashMap<String, ArrayList<String>>();
    for(int i = 0; i < arr.length; i++){
        // arr에 담긴 데이터를 ,를 기준으로 split하여 변수 line에 담음
        String[] line = arr[i].split(",");
        // line에 담긴 내용 중 6번째 내용(line[5]) 를 변수 key에 담음
        String key = line[5];
        //list라는 이름으로 arraylist를 선언
        ArrayList<String> list = new ArrayList<String>();
        // key가 dic(hashmap)에 있는지 확인
        if (dic.containsKey(key)){  // 있다면 list에 담긴 value 가져오고 line의 12번째 내용을 추가
            list = dic.get(key)
            list.add(line[13])
        }else{  // 없다면 list에 line의 12번째 내용을 추가
            list.add(line[13]);
        }
        // 변수 key를 dic의 key값으로, 변수 list를 dic의 value값으로 추가
        dic.put(key,list);
        // 정상적으로 해시맵에 들어갔는지 확인
        for (String key:dic.keySet()){
            System.out.println(key);
        }

        return dic;

    }
}

```

#### 5) HashMap Value 기준으로 정렬 - Entry 내장 함수 사용
```java
Map<String, Integer> map = new HashMap<>();
map.put("a",3);
map.put("b",2);
map.put("c",1);
List<Map.Entry<String,Integer>> entryList = new LinkedList<>(map.entrySet());

entryList.sort(Map.Entry.comparingByValue());
for(Map.Entry<String,Integer> entry: entryList){
    System.out.println("key : " + entry.getKey() + ", value : " + entry.getValue());
}

//key : c, value : 1
//key : b, value : 2
//key : a, value : 3
```


### (2) 간단 요약

#### 라이브러리
```java
import java.util.*;
import java.io.*;
```
#### 길이
- length : 배열(Array) 길이
- length() : 문자열(String) 길이
- size() : Collections 객체 - list길이
```java
int[] arr = new arr[3];
System.out.println(arr.length)

String str = "java";
System.out.println(str.length())

ArrayList<Integer> list = new ArrayList<>();
System.out.println(list.size())
```

#### 정렬
- Array : Arrays.sort(배열);
- ArrayList : Collections.sort(리스트);
```java
int[] arr = {2,3,1,5,3};
Arrays.sort(arr);

List<Integer> list = new ArrayList<>(Arrays.asList(arr));
Collections.sort(list);
```

#### Math 라이브러리
```java
Math.max(10,2)  // 최대
Math.min(10,2)  // 최소

Math.abs(-1);     // 절대값

Math.ceil(-3.2)     // 올림 (-3)
Math.floor(-3.2)    // 내림 (-4)
Math.round(-3.26)   // 첫째자리에서 반올림(-3)

// 반올림 자리수 지정
double a = 1.23456;
String b = String.format("%.1f",a);     // 둘째자리 반올림

// 제곱, 제곱근
Math.pow(2,2);  // 4
Math.sqrt(4);   // 2
```

#### 자료형 변환
```java
char c='5';
String s=new String('1324');
String s2=new String('01101');
int n = 3;
char[] name='Jade Song';   // char형 배열에 각각의 문자가 그대로 저장되어있음
// char -> int
int res1 = c - '0';
// String -> int
int res2 = Integer.parseInt(s);
// String(n진수) -> int
int res3 = Integer.parseInt(s2,2);
// int -> String(n진수)
String str = Integer.toString(n);
String str2 = Integer.toString(res3,2);
// char[] -> String 변환
String str3 = String.valueOf(char[] name);
```
