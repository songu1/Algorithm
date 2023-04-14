# 코딩테스트를 위한 자바 문법
- **import java.util.*;** 꼭 포함시켜서 풀이하기!

## [1] ArrayList
### (1) 깊은 복사
- 복사되는 배열.addAll(복사할 배열)
```java
public class Main(){
    public static void main(String[] args) {
        ArrayList<Integer> w = new ArrayList<Integer>();
        ArrayList<Integer> copy_w = new ArrayList<Integer>();
        copy_w.addAll(w);
    }
}
```
### (2) Sort
- 리스트명.sort()
```java
public class Main(){
    public static void main(String[] args) {
        ArrayList<Integer> ArrList = new ArrayList<Integer>();
        ArrList.sort(null);
    }
}
```
### (3) Size
- 리스트명.size()
```java
public class Main(){
    public static void main(String[] args) {
        ArrayList<Integer> ArrList = new ArrayList<Integer>();
        ArrList.size();
    }
}
```
## [2] List
- set -> List 변경
- 

## [3] Array

## [4] Set

## [5] Map

## [6] String

## [7] StringBuilder

## [8] 입출력

## [9] Queue

## [10] Priority Queue


<hr>

## [1] 문자열
### 1. 조건 판단
- 대문자인지 소문자인지 확인
- 문자가 숫자인지 확인
- 소문자 <-> 대문자 변환
- 대소문자 무시하고 두 문자열 비교
```java
public class Solution(){
    public static void main(String[] args) {
        String s=new String("Ab1cdefg");
        String s2=new String("aB1CdeFg");
        char ch=s.charAt(0);    // A
        char ch2=s.charAt(1);   // b
        char ch3=s.charAt(2);   // 1
// 대문자인지 확인
        if(Character.isUpperCase(ch))
            System.out.println("Upper");
// 소문자인지 확인
        if(Character.isLowerCase(ch2))
            System.out.println("Lower");
// 문자가 숫자인지 확인
        if(Character.isDigit(ch3))
            System.out.println("number");
// 소문자 -> 대문자
        char bigChar=Character.toUpperCase(ch2);
// 대문자 -> 소문자
        char smallChar=Character.toLowerCase(ch1);
// 대소문자 무시하고 두 문자열 비교
        s.equalsIgnoreCase(s2);
    }
}
```
### 2. 다른 자료형과 형변환
- char -> int
- String -> int
- String(n진수) -> int
- int -> String
- char[] -> String
```java
public class Solution(){
    public static void main(String[] args) {
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
    }
}
```
### 3. 알고리즘 구현 관련
- 문자열 for-each문
- 숫자 비교
- split
- indexOf
- substring
- 문자열 뒤집기
- replaceAll
- replace
- 대칭 비교
- 

