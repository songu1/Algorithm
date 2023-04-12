# 자바 문법
## [1] 입출력
### 표준입출력
- 표준 입력
```java
import java.util.*;
public class Solution(){
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("문장을 입력하시오");
        String line=input.nextLine();
    }
}
```
### ★★Scanner 클래스의 주요 메소드★★★
| 메소드 | 설명 |
| --- | --- |
| String next() | 다음 토큰을 문자열로 리턴 |
| byte nextByte() | 다음 토큰을 byte 타입으로 리턴 |
| short nextShort() | 다음 토큰을 short 타입으로 리턴 |
| int nextInt() | 다음 토큰을 int 타입으로 리턴 |
| long nextLong() | 다음 토큰을 long 타입으로 리턴 |
| float nextFloat() | 다음 토큰을 float 타입으로 리턴 |
| double nextDouble() | 다음 토큰을 double 타입으로 리턴 |
| boolean nextBoolean() | 다음 토큰을 boolean 타입으로 리턴 |
| String nextLine() | '\n'을 포함하는 한 라인을 읽고 '\n'을 버린 나머지만 문자열로 리턴 |
| void close() | Scanner의 사용 종료 |
| boolean hasNext() | 현재 입력된 토큰이 있으면 true, 아니면 새로운 입력이 있을 때 까지 무한정 대기. 새로운 입력이 들어올 때 true 리턴. ctrl+z 키가 입력되면 입력의 끝이므로 false 리턴 |
- char형은 string으로 받은 후 charAt해주기

### 문자열 입력 받기
```java
import java.util.*;
public class Solution(){
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("출력");
        String line=input.nextLine();   // 한줄 읽기
        int number=input.nextInt();
    }
}
```

## [2] 조건문
### if else
```java
public class Solution(){
    public static void main(String[] args) {
        if(조건){
            System.out.println('a');
        }
        else if(조건){
            System.out.println('a');
        }
        else{
            System.out.println('a');
        }
    }
}
```

### switch
```java
public class Solution(){
    public static void main(String[] args) {
        switch(변수){
            case c1:
                command1;
                break;
            case c2:
                command2;
                break;
            ...
            default:
                commandD;
                break;
        }
    }
}
```

### 조건 연산자
- opr1 ? op2 : opr3

## [3] 반복문
### while, do~while
```java
public class Solution(){
    public static void main(String[] args) {
        while(조건식){
            // command
        }
        
        do{
            // command
        }while(조건식);
    }
}
```

### for문, for-each
```java
public class Solution(){
    public static void main(String[] args) {
        for(초기식;조건식;증감식){
            // command
        }
        
        for(변수:배열){
            // command
        }
    }
}
```

## [4] 배열
### 1차원 배열
1. 배열 선언
   - 배열 참조 변수
   ```java
    int intArray[];
    int[] intArray2;
    ```
2. 배열 생성
   - new 연산자 생성
    ```java
    intArray = new int[5];
    // 선언과 동시에 배열 생성
    int intArray[] = new int[5];
    ```
3. 배열 초기화
    ```java
    // new 키워드를 통해 생성과 동시에 초기화
    int Array[] = new int[]{10,20,30};
    // new 키워드 생략가능, 암시적으로 생성
    int Array2[] = {10,20,30};
    // 선언부와 분리
    int Array3[];
    Array3 = new int[]{10,20,30};
    ```

### 2차원 배열
```java
int[][] testArray={
        {10,20,30},
        {40,50,60},
        {70,80,90}
}
// 행의 크기만 생성 후 각 행에 해당하는 열의 크기는 다르게 생성
int[][] xy=new int[5][];
xy[0]=new int[1];
xy[1]=new int[2];
xy[2]=new int[3];
xy[3]=new int[4];
xy[4]=new int[5];

//열의 크기가 다른 배열
int[][]xy={
{10,20},
{30,40,50},
{60,70,80,90}
};
```

## [5] 
