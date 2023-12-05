# SQL 코딩테스트용 문법 (MySQL)
순서
SELECT - DISTINCT - FROM - JOIN - ON - WHERE - GROUP BY - HAVING - ORDER BY - LIMIT - OFFSET

## [1] DATE

### (1) 날짜를 문자열로 데이터 형식 지정 (날짜 -> 문자)
```SQL
SELECT DATE_FORMAT(CREATE_DATE, '%y-%m-%d') AS CREATE_DATE
FROM TEST;
```
- %Y : 연도4자리
- %y : 연도2자리
- %M : 월 영어
- %m : 월 숫자(2자리)
- %c : 월 숫자(1자리)
- %D : 일 영어(1st, 2nd, ...)
- %d : 일 숫자(2자리)
- %j : 일 숫자(1년 단위)
- %e : 일 숫자(1자리)
- %H : 시 24시간(2자리)
- %h : 시 12시간(2자리)
- %i : 분 2자리
- %s, %S : 초 2자리
- %W : 요일 (Monday,Tuesday,...)
- %w : 요일 (0=Sunday, )

### (2) 날짜 유형 데이터에서 연도, 월, 일 추출
- DATE(날짜)
- MONTH(날짜)
- YEAR(날짜)
- HOUR(날짜)
- MINUTE(날짜)
- SECOND(날짜)
- WEEKDAY(날짜)

## [2] 조건문

### IF
- SELECT, WHERE절에서 사용 가능
- 3중 연산자 느낌
```sql
SELECT IF(10>5, '크다','작다') AS result;
```
### IFNULL
- IFNULL(NAME,'No name') : 컬럼 값이 NULL일 경우 'No name'으로 대체
```sql
SELECT IFNULL(컬럼명, "Null일경우 대체값")
FROM 테이블명;
```

### CASE 문
```SQL
CASE
    WHEN 조건1 THEN 실행1
    WHEN 조건2 THEN 실행2
    ELSE 실행3
END

SELECT PT_NAME, PT_NO, GEND_CD, AGE,
    CASE WHEN TLNO IS NULL THEN 'NONE'
    ELSE TLNO END
FROM PATIENT;
```

## [3] 특정 개수만 출력
### LIMIT
- LIMIT ROW수
```SQL
SELECT 컬럼명
FROM 테이블명
WHERE 조건식
LIMIT ROW수;

SELECT * FROM A
LIMIT 0,3;      -- 0번부터 3개 RETURN
```

### 1~N까지 번호매기기
- SELELT @변수이름 := 대입값;
```SQL
SELECT @ROWNUM := @ROWNUM + 1 AS ROWNUM, A.*
FROM TABLEA A, (SELECT @ROWNUM := 0) TMP;
```

## [4] 함수
### (1) 숫자 관련 함수
- ROUND(컬럼명, 반올림할 소수점 자릿수 지정)
```SQL
SELECT ROUND(10.349,1)  -- 10.3
SELECT ROUND(11.546,-1) -- 10
```
- CEILING(컬럼명) : 올림
- FLOOR(컬럼명) : 내림

## [5] 문자열
### (1) 문자열 슬라이싱
- 인덱스 1부터 시작
#### SUBSTRING
- 원하는 위치부터 길이까지 자르기
```SQL
SELECT SUBSTRING("문자열",시작위치);    -- 시작위치부터 끝까지
SELECT SUBSTRING("문자열",시작위치, 길이);
```
#### LEFT/RIGHT
- 문자열을  왼쪽/오른쪽부터 잘라내기
```SQL
SELECT LEFT("문자열",길이);
SELECT RIGHT("문자열",길이);
```

### (2) 문자열 대문자 <-> 소문자
- LOWER(컬럼명) : 소문자로
- UPPER(컬럼명) : 대문자로

### (3) 문자열 MAX,MIN하기
- 한글을 제외한 문자 : ASCII 코드를 사용
    - 영어 : 대문자 < 소문자
    - 뒤의 알파벳이 큰수로
- 한글 : UNICODE사용
    - 자음 < 모음 < 한글
- 한글, 영문, 숫자, 특수문자 함께
    - 특수문자 < 숫자 < 숫자(특) < 영문 < 영문(특) < 한글 < 한글(특)
- MAX : NULL값을 무시

### (4) 문자 <-> 숫자
- CAST(변환대상 AS TYPE)
- CONVERT(변환대상, TYPE)
    - BINARY
    - CHAR(개수)
    - DATE
    - DATETIME
    - SIGNED : 부호있는 숫자
    - UNSIGNED : 부호없는 숫자
#### 문자 -> 숫자
```SQL
SELECT CAST('123' AS UNSIGNED) FROM DUAL
```
#### 숫자 -> 문자
```SQL
SELECT CAST(123 AS CHAR(3)) FROM DUAL;
SELECT CONVERT(13341, CHAR);
```
#### 문자/숫자 -> 날짜
```SQL
SELECT CAST(20220302 AS DATE) FROM DUAL;
SELECT CAST('20220302' AS DATE) FROM DUAL;
```
