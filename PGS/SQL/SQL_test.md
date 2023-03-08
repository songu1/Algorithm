# SQL 코딩테스트용 문법 (Oracle)

## [1] DATETIME(날짜,시간)

### (1) 날짜 유형의 데이터로부터 연도, 월, 일, 시간 추출
- EXTRACT 함수
    - 날짜 유형의 데이터로부터 날짜 정보를 분리하여 새로운 컬럼의 형채로 추출해주는 함수
- EXTRACT('날짜요소' FROM 컬럼명)
    - 날짜 요소 : YEAR, MONTH, DAY, HOUR, MINUTE, SECOND
```sql
EXTRACT(YEAR FROM birthday)
```

### (2) 날짜 -> 문자
- TO_CHAR(컬럼명,'날짜형태')
```sql
TO_CHAR(birthday,'yyyy-mm-dd')
```

### (3) 날짜 -> 숫자
- TO_NUMBER(TO_CHAR(컬럼명, '날짜형태'))
```SQL
SELECT TO_NUMBER(TO_CHAR(DATETIME,'HH24')) AS HOUR
FROM ANIMAL_OUTS;
```

### (4) 문자 -> 날짜
- TO_DATE(날짜 문자열, 날짜형태)
```SQL
TO_DATE('2023-02-03','YYYY-MM-DD')
```

## [2] 조건문

### (1) CASE WHEN
```sql
CASE WHEN 조건 THEN 실행
ELSE 실행
END

-- EX
SELECT PT_NAME, PT_NO, GEND_CD, AGE,
    CASE WHEN TLNO IS NULL THEN 'NONE'
    ELSE TLNO END
FROM PATIENT;
```

## [3] NULL

### (1) IS NULL / IS NOT NULL
```SQL
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL;
```

## [4] 함수

### (1) 숫자 관련 함수
- ROUND(컬럼명,나타낼 자릿수) : 반올림
- FLOOR(컬럼명,나타낼 자릿수) : 내림

### (2) 집계함수
- SELECT, HAVING절에서만 사용가능

### (1) INTERSECT, UNION, EXCEPT
```SQL
(SELECT ...
FROM ...
WHERE ...)
INTERSECT/UNION/EXCEPT
(SELECT ...
FROM ...
WHERE ...)
```

## [5] 문자열

### (1) 문자열 슬라이싱
- SUBSTR("문자열","시작위치","길이")
```SQL
SELECT SUBSTR(PRODUCT_COD,1,2) AS CATEGORY
FROM PRODUCT;
```

### (2) 문자열 대문자 -> 소문자 / 소문자 -> 대문자
- LOWER(컬럼명) : 소문자로
- UPPER(컬럼명) : 대문자로

### (3) 문자열 MAX, MIN하기
- 한글을 제외한 문자 : ASCII 코드를 사용
    - 영어 : 대문자 < 소문자
    - 뒤의 알파벳이 큰수로
- 한글 : UNICODE사용
    - 자음 < 모음 < 한글
- 한글, 영문, 숫자, 특수문자 함께
    - 특수문자 < 숫자 < 숫자(특) < 영문 < 영문(특) < 한글 < 한글(특)
- MAX : NULL값을 무시


## [6] 중첩쿼리

### (1) IN
```SQL
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD , MAX(FAVORITES)
                                FROM REST_INFO
                                GROUP BY FOOD)
```

## [7] SELECT

### (1) 특정 개수만 출력
1. **ROWNUM** 키워드 사용
- ROWNUM : 조회된 순서대로 순번을 매김
    ```SQL
    SELECT ROWNUM, a.* FROM emp a;
    ```
- ORDER BY를 수행하면 섞임 -> 정렬된 서브쿼리으 결과에 순번을 매겨야함
    ```SQL
    SELECT ROWNUM, x.*   
    FROM ( SELECT a.* FROM emp a ORDER BY a.ename) x;
    ```
- 예시
    ```SQL
    SELECT NAME, DATETIME
    FROM (SELECT I.NAME, I.DATETIME
        FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O
        ON I.ANIMAL_ID=O.ANIMAL.ID
        WHERE O.ANIMAL_ID IS NULL
        ORDER BY DATETIME)
    WHERE ROWNUM <= 10;
    ```

2. **ROW_NUMBER()** 함수 사용
- ROW_NUMBER() : 그룹별 순번을 반환해줌
- ROW_NUMBER() OVER(PARTITION BY [그룹컬럼] ORDER BY [정렬컬럼])
    - 정렬컬럼은 필수
```SQL
SELECT ROW_NUMBER() OVER(ORDER BY E.job, E.name) ROW_NUM, E.*
FROM EMP E ORDER BY E.job, E.name;
```

### (2) 1~N까지 숫자 조회
```SQL
-- 1부터 10까의 숫자를 조회
SELECT LEVEL AS NO
FROM DUAL
CONNECT BY LEVEL <=10;
```

## [8] JOIN

### (1) OUTER JOIN
- A LEFT(RIGHT) OUTER JOIN B ON A.ID=B.ID


## [9] 임시테이블

### (1) WITH
```sql
WITH EMP_W AS
(SELECT DEPTNO, SUM(SAL) AS SAL
FROM EMP
GROUP BY DEPTNO
)

SELECT * FROM EMP_W
```