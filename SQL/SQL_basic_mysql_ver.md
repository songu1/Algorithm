# SQL 기본 문법 (MySQL 8.0 기준)

## 실행 순서
작성 순서: SELECT - DISTINCT - FROM - JOIN - ON - WHERE - GROUP BY - HAVING - ORDER BY - LIMIT - OFFSET
실제 실행 순서: FROM → JOIN/ON → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT
- WHERE에서는 SELECT의 별칭(AS)을 못 쓰지만, ORDER BY/HAVING에서는 쓸 수 있다. (MySQL은 HAVING에서도 별칭 허용)

## 기본 쿼리
```sql
SELECT <컬럼>
FROM <테이블명>
WHERE <조건>
GROUP BY <그룹화할 컬럼>   -- 결과를 그룹으로 묶음
HAVING <조건>              -- 그룹에 대한 조건
ORDER BY <컬럼명> ASC/DESC -- 기본 ASC
LIMIT n;
```

## Table as Sets

### DISTINCT : 중복 제거
```sql
SELECT DISTINCT Salary FROM EMPLOYEE;
SELECT COUNT(DISTINCT Dno) FROM EMPLOYEE;   -- 중복 제외 개수
```

### 합집합 : UNION / UNION ALL
- UNION : 중복 제거
- UNION ALL : 중복 포함 (더 빠름, 중복 걱정 없으면 이걸 사용)
- 두 SELECT의 컬럼 개수와 타입이 같아야 함
```sql
SELECT name FROM customer
WHERE address LIKE '대한민국%'
UNION
SELECT name FROM customer
WHERE custid IN (SELECT custid FROM orders);
```

### 교집합 : INNER JOIN 또는 IN/EXISTS
MySQL은 8.0.31 이전에는 INTERSECT가 없으므로 아래 방식 사용
```sql
SELECT DISTINCT A.str
FROM tableA A
JOIN tableB B ON A.str = B.str;

-- 또는
SELECT DISTINCT str FROM tableA
WHERE str IN (SELECT str FROM tableB);
```

### 차집합 : NOT IN / NOT EXISTS / LEFT JOIN ... IS NULL
MINUS(Oracle), EXCEPT(MySQL 8.0.31+)는 쓰지 않는다.
```sql
-- (1) NOT IN : 서브쿼리 결과에 NULL이 있으면 결과가 비는 함정 주의
SELECT str FROM tableA
WHERE str NOT IN (SELECT str FROM tableB WHERE str IS NOT NULL);

-- (2) NOT EXISTS : NULL에 안전, 권장
SELECT A.str FROM tableA A
WHERE NOT EXISTS (SELECT 1 FROM tableB B WHERE B.str = A.str);

-- (3) LEFT JOIN + IS NULL
SELECT A.str
FROM tableA A
LEFT JOIN tableB B ON A.str = B.str
WHERE B.str IS NULL;
```

### 대칭차집합
```sql
SELECT str FROM tableA WHERE str NOT IN (SELECT str FROM tableB WHERE str IS NOT NULL)
UNION ALL
SELECT str FROM tableB WHERE str NOT IN (SELECT str FROM tableA WHERE str IS NOT NULL);
```

## 기타 연산

### 패턴 매칭 LIKE
- % : 0개 이상의 문자
- _ : 정확히 1개의 문자
```sql
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Address LIKE '%Houston, TX%';

SELECT Fname, Lname
FROM EMPLOYEE
WHERE Bdate LIKE '199_-__-__';      -- 날짜(YYYY-MM-DD) 문자열 패턴

-- 정규식 (MySQL)
SELECT * FROM T WHERE name REGEXP '^[A-C]';   -- A~C로 시작
```
- 대소문자: MySQL 기본 collation은 대소문자 구분 안 함 (LIKE도 마찬가지)

### 산술/비교 연산
- +, -, *, /, %(MOD)
- `/`는 MySQL에서 나눗셈 결과가 소수(DECIMAL)로 나옴. 정수 나눗셈은 `DIV`
- BETWEEN a AND b : a 이상 b 이하 (양 끝 포함)
- IN (a, b, c), NOT IN (...)
- 같지 않음: `!=` 또는 `<>`

### NULL, EMPTY 체크
- NULL : `IS NULL` / `IS NOT NULL` (값이 없음)
- EMPTY : `= ''` / `!= ''` (빈 문자열)
- NULL과의 비교(`= NULL`)는 항상 NULL(거짓) 취급 → 반드시 IS NULL 사용
```sql
SELECT * FROM BOARD WHERE TITLE IS NOT NULL;
SELECT * FROM BOARD WHERE TITLE != '';
SELECT * FROM BOARD WHERE TITLE IS NULL OR TITLE = '';
```

## 중첩쿼리

```sql
-- Smith가 manager나 employee로 일하고 있는 프로젝트 번호를 중복 없이 검색
SELECT DISTINCT Pnumber FROM PROJECT
WHERE Pnumber IN
    (SELECT P.Pnumber FROM PROJECT P, DEPARTMENT D, EMPLOYEE E
     WHERE P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND E.Lname = 'Smith')
   OR Pnumber IN
    (SELECT Pno FROM WORKS_ON, EMPLOYEE
     WHERE Essn = Ssn AND Lname = 'Smith');
```

### IN
- 집합 비교 연산자, WHERE절에서 사용
- MySQL은 여러 컬럼 동시 비교 `(a, b) IN (SELECT ...)` 가능
```sql
SELECT DISTINCT Essn FROM WORKS_ON
WHERE (Pno, Hours) IN (SELECT Pno, Hours
                       FROM WORKS_ON
                       WHERE Essn = '123456789');
```

### ALL / ANY
```sql
SELECT Lname, Fname
FROM EMPLOYEE
WHERE Salary > ALL (SELECT Salary FROM EMPLOYEE WHERE Dno = 5);
-- ALL : 모든 값보다 큼 (= 최댓값보다 큼)
-- ANY : 하나라도 만족 (= 최솟값보다 큼)

-- 같은 의미를 MAX로 (코테에서는 이쪽이 더 읽기 쉬움)
SELECT Lname, Fname FROM EMPLOYEE
WHERE Salary > (SELECT MAX(Salary) FROM EMPLOYEE WHERE Dno = 5);
```

### (NOT) EXISTS
- 상관 서브쿼리의 결과가 비었는지 확인 → TRUE/FALSE
- 서브쿼리 안은 `SELECT 1`로 써도 됨 (값은 상관없음)
```sql
-- 부양가족이 있는 직원
SELECT Fname, Lname FROM EMPLOYEE E
WHERE EXISTS (SELECT 1 FROM DEPENDENT D WHERE D.Essn = E.Ssn);

-- 부양가족이 없는 직원
SELECT Fname, Lname FROM EMPLOYEE E
WHERE NOT EXISTS (SELECT 1 FROM DEPENDENT D WHERE D.Essn = E.Ssn);
```

#### NOT EXISTS 이중 부정 (모든 ~를 한 경우, 관계 나눗셈)
"5번 부서가 관리하는 모든 과제에 참여한 직원" = "참여하지 않은 5번 부서 과제가 존재하지 않는 직원"
EXCEPT/MINUS 대신 NOT EXISTS 두 겹으로 쓴다 (MySQL 모든 버전 가능).
```sql
SELECT E.Fname, E.Lname
FROM EMPLOYEE E
WHERE NOT EXISTS (
    SELECT 1
    FROM PROJECT P
    WHERE P.Dnum = 5
      AND NOT EXISTS (
          SELECT 1
          FROM WORKS_ON W
          WHERE W.Essn = E.Ssn
            AND W.Pno = P.Pnumber
      )
);
```
(코테에서는 보통 `GROUP BY ... HAVING COUNT(DISTINCT ...) = (전체 개수)` 방식으로도 풀 수 있음)

## JOIN

### 암시적 조인 (콤마)
```sql
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A, 테이블명 B
WHERE A.ID = B.ID AND A.NAME = 'Research';
```

### JOIN = INNER JOIN (교집합, 양쪽 모두에 있는 행)
```sql
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A INNER JOIN 테이블명 B ON A.ID = B.ID;
```
- JOIN만 써도 INNER JOIN과 같음

### LEFT JOIN
- 왼쪽 테이블은 전부, 오른쪽에 매칭이 없으면 NULL
```sql
-- 왼쪽 전체 (공통 + 왼쪽만)
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A LEFT JOIN 테이블명 B ON A.ID = B.ID;

-- 왼쪽에만 있는 것 (공통 제외)
SELECT A.컬럼명
FROM 테이블명 A LEFT JOIN 테이블명 B ON A.ID = B.ID
WHERE B.ID IS NULL;
```

### RIGHT JOIN
```sql
-- 오른쪽 전체
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A RIGHT JOIN 테이블명 B ON A.ID = B.ID;

-- 오른쪽에만 있는 것
SELECT B.컬럼명
FROM 테이블명 A RIGHT JOIN 테이블명 B ON A.ID = B.ID
WHERE A.ID IS NULL;
```
- 헷갈리면 RIGHT JOIN은 테이블 순서를 바꿔서 LEFT JOIN으로 쓰는 게 안전

### FULL OUTER JOIN 대체
MySQL은 FULL OUTER JOIN이 없으므로 LEFT + UNION + RIGHT
```sql
SELECT * FROM A LEFT JOIN B ON A.ID = B.ID
UNION
SELECT * FROM A RIGHT JOIN B ON A.ID = B.ID;
```

### SELF JOIN
```sql
-- 직원과 그 직원의 상사 이름
SELECT E.Fname AS emp, S.Fname AS boss
FROM EMPLOYEE E
LEFT JOIN EMPLOYEE S ON E.Super_ssn = S.Ssn;
```

### LEFT JOIN 주의점
오른쪽 테이블 조건을 WHERE에 쓰면 LEFT JOIN이 INNER JOIN처럼 동작한다. 조건은 ON에 쓴다.
```sql
-- 조건을 ON에 쓰면 왼쪽 행이 유지됨
FROM A LEFT JOIN B ON A.ID = B.ID AND B.TYPE = 'X'
```

## 집계함수
- COUNT, SUM, MAX, MIN, AVG
- **MEDIAN은 MySQL에 없음** → 중앙값은 윈도우 함수로 직접 구함 (아래 참고)
- NULL은 제외하고 계산 (단 `COUNT(*)`는 NULL 행도 센다)
    - `COUNT(*)` : 전체 행 수
    - `COUNT(컬럼)` : 그 컬럼이 NULL이 아닌 행 수
    - `COUNT(DISTINCT 컬럼)` : 중복 제외
- 집계함수는 SELECT, HAVING, ORDER BY절에서 사용 (WHERE에는 못 씀)
- 값이 하나도 없을 때 SUM/AVG는 NULL → `IFNULL(SUM(x), 0)`

## GROUP BY
- 그룹화 후 집계 실행
- SELECT에는 **GROUP BY에 쓴 컬럼 또는 집계함수**만 쓸 수 있음 (MySQL 8.0 기본 ONLY_FULL_GROUP_BY)
- WHERE : 그룹 만들기 전 행 필터
- HAVING : 그룹 만든 뒤 그룹 필터 (집계함수 조건)
```sql
SELECT Dno, COUNT(*) AS cnt, AVG(Salary) AS avg_sal
FROM EMPLOYEE
WHERE Salary > 0
GROUP BY Dno
HAVING COUNT(*) >= 2
ORDER BY cnt DESC;
```
- 여러 컬럼 그룹: `GROUP BY year, month`
- 그룹별 문자열 합치기: `GROUP_CONCAT(name ORDER BY name SEPARATOR ',')`

## WITH (CTE, 가상테이블) - MySQL 8.0 이상
- 쿼리 실행 중에만 쓰는 임시 테이블
```sql
WITH 가상테이블명 AS (
    SELECT 컬럼A, COUNT(*) AS cnt
    FROM 테이블명
    WHERE 조건
    GROUP BY 컬럼A
)
SELECT B.컬럼B, A.cnt
FROM 테이블명 B JOIN 가상테이블명 A ON A.컬럼A = B.컬럼A;
```
- 여러 개: `WITH a AS (...), b AS (...) SELECT ...`

---

# 코테 빈출 패턴

## 1. 윈도우 함수 (MySQL 8.0+)
```sql
함수() OVER (PARTITION BY 그룹컬럼 ORDER BY 정렬컬럼)
```
```sql
-- 그룹 내 순위
SELECT name, dept, salary,
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn,     -- 1,2,3,4 (동점도 다른 번호)
    RANK()       OVER (PARTITION BY dept ORDER BY salary DESC) AS rk,     -- 1,2,2,4 (동점 후 건너뜀)
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS drk     -- 1,2,2,3 (건너뛰지 않음)
FROM EMP;

-- 그룹별 TOP N: 윈도우 함수는 WHERE에 못 쓰므로 CTE/서브쿼리로 감싼다
WITH t AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rk
    FROM EMP
)
SELECT * FROM t WHERE rk <= 3;

-- 이전/다음 행
LAG(col, 1)  OVER (ORDER BY dt)    -- 이전 행 값
LEAD(col, 1) OVER (ORDER BY dt)    -- 다음 행 값

-- 누적합 / 그룹 전체 합 / 비율
SUM(amount) OVER (ORDER BY dt)                          -- 누적합
SUM(amount) OVER (PARTITION BY dept)                    -- 그룹 합 (행 유지)
amount / SUM(amount) OVER () AS ratio                   -- 전체 대비 비율

-- 상위 n% 등급 나누기
NTILE(4) OVER (ORDER BY score DESC)                     -- 4분위
PERCENT_RANK() OVER (ORDER BY score)                    -- 0~1 상대 순위
```

## 2. 중앙값 (MEDIAN 대체)
```sql
SELECT AVG(val) AS median
FROM (
    SELECT val,
           ROW_NUMBER() OVER (ORDER BY val) AS rn,
           COUNT(*) OVER () AS cnt
    FROM T
) x
WHERE rn IN (FLOOR((cnt + 1) / 2), CEIL((cnt + 1) / 2));
```

## 3. 조건부 집계
```sql
SELECT dept,
    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_cnt,
    COUNT(CASE WHEN gender = 'F' THEN 1 END)      AS female_cnt,   -- CASE의 ELSE 없으면 NULL → COUNT가 제외
    SUM(IF(status = 'DONE', 1, 0))                AS done_cnt
FROM EMP
GROUP BY dept;
```
- 비율: `ROUND(SUM(CASE WHEN ... THEN 1 ELSE 0 END) / COUNT(*) * 100, 1)`
- 조건 평균: `AVG(IF(cond, val, NULL))`

## 4. NULL 처리
```sql
IFNULL(col, 0)                  -- 2개 인자
COALESCE(col1, col2, 0)         -- 처음으로 NULL이 아닌 값
NULLIF(a, b)                    -- a=b면 NULL (0으로 나누기 방지: x / NULLIF(y, 0))
```

## 5. 날짜 계산
```sql
DATEDIFF('2024-03-10', '2024-03-01')       -- 9 (일 차이, 앞 - 뒤)
DATE_ADD(dt, INTERVAL 7 DAY)               -- 7일 뒤 (MONTH, YEAR 등도 가능)
DATE_SUB(dt, INTERVAL 1 MONTH)             -- 1달 전
TIMESTAMPDIFF(MONTH, start_dt, end_dt)     -- 단위 지정 차이 (끝 - 시작)
LAST_DAY(dt)                               -- 그 달의 마지막 날
CURDATE(), NOW()
WHERE dt >= '2024-01-01' AND dt < '2024-02-01'   -- 기간 조건 (DATETIME이면 BETWEEN보다 안전)
-- 요일: DAYOFWEEK() 1=일요일 ~ 7=토요일, WEEKDAY() 0=월요일 ~ 6=일요일
```

## 6. 재귀 CTE: 없는 값을 만들어서 LEFT JOIN (0~23시 등)
```sql
WITH RECURSIVE hours AS (
    SELECT 0 AS h
    UNION ALL
    SELECT h + 1 FROM hours WHERE h < 23
)
SELECT h.h AS HOUR, COUNT(o.ID) AS COUNT
FROM hours h
LEFT JOIN ANIMAL_OUTS o ON HOUR(o.DATETIME) = h.h
GROUP BY h.h
ORDER BY h.h;
```

## 7. 자주 쓰는 패턴
```sql
-- 중복 값 찾기
SELECT name FROM T GROUP BY name HAVING COUNT(*) > 1;

-- 최댓값을 가진 행 (동점 모두)
SELECT * FROM T WHERE val = (SELECT MAX(val) FROM T);

-- 정렬 후 하나만: ORDER BY ... LIMIT 1
-- 정렬 기준이 같을 때를 대비해 보조 정렬 키 추가: ORDER BY cnt DESC, id ASC

-- 문자열
-- CONCAT(a, b), SUBSTRING(s, 시작(1부터), 길이), LEFT(s, n), RIGHT(s, n)
-- LENGTH(s) (바이트), CHAR_LENGTH(s) (글자 수)
-- REPLACE(s, 'a', 'b'), TRIM(s), UPPER(s), LOWER(s), LPAD(s, 3, '0')
```

---

# MySQL 전용 문법

## [1] DATE

### (1) 날짜 -> 문자열 (DATE_FORMAT)
```sql
SELECT DATE_FORMAT(CREATE_DATE, '%Y-%m-%d') AS CREATE_DATE
FROM TEST;
```
- %Y : 연도 4자리, %y : 연도 2자리
- %M : 월 영어(March), %m : 월 숫자 2자리(03), %c : 월 숫자 1자리(3)
- %D : 일 영어(1st), %d : 일 숫자 2자리(01), %e : 일 숫자 1자리(1)
- %j : 1년 중 몇 번째 날
- %H : 시 24시간(00~23), %h : 시 12시간(01~12)
- %i : 분 2자리 (**%m이 아니라 %i**)
- %s, %S : 초 2자리
- %W : 요일 영어(Monday), %w : 요일 숫자(0=일요일)

### (2) 연도/월/일 추출
- DATE(dt), YEAR(dt), MONTH(dt), DAY(dt)
- TIME(dt), HOUR(dt), MINUTE(dt), SECOND(dt)
- WEEKDAY(dt) : 0=월요일

## [2] 조건문
```sql
IF(10 > 5, '크다', '작다')               -- 삼항 연산자 느낌, SELECT/WHERE에서 사용
IFNULL(컬럼명, 'No name')                -- NULL이면 대체값
CASE
    WHEN 조건1 THEN 값1
    WHEN 조건2 THEN 값2
    ELSE 값3
END
```
```sql
SELECT PT_NAME, PT_NO, GEND_CD, AGE,
    CASE WHEN TLNO IS NULL THEN 'NONE' ELSE TLNO END AS TLNO
FROM PATIENT;
```

## [3] 특정 개수만 출력
```sql
SELECT * FROM A LIMIT 3;          -- 처음 3개
SELECT * FROM A LIMIT 0, 3;       -- offset 0부터 3개
SELECT * FROM A LIMIT 3 OFFSET 0; -- 위와 동일
```

### 번호 매기기
```sql
-- MySQL 8.0 이상 (권장)
SELECT ROW_NUMBER() OVER (ORDER BY id) AS ROWNUM, S.*
FROM students S;

-- 8.0 미만 (변수 방식)
SELECT @ROWNUM := @ROWNUM + 1 AS ROWNUM, A.*
FROM TABLEA A, (SELECT @ROWNUM := 0) TMP;
```

## [4] 숫자 함수
```sql
ROUND(10.349, 1)    -- 10.3
ROUND(11.546, -1)   -- 10
CEILING(x), FLOOR(x), TRUNCATE(x, 자리)
ABS(x), MOD(a, b), POWER(a, b)
```

## [5] 문자열
- 인덱스는 1부터 시작
```sql
SUBSTRING('문자열', 시작위치)
SUBSTRING('문자열', 시작위치, 길이)
LEFT('문자열', 길이), RIGHT('문자열', 길이)
CONCAT('a', 'b', 'c')
LOWER(col), UPPER(col)
```
- MAX/MIN : NULL 무시. 문자열은 정렬 규칙(collation)에 따름

## [6] 형변환
```sql
CAST(변환대상 AS 타입)
CONVERT(변환대상, 타입)
-- 타입: SIGNED, UNSIGNED, CHAR, DATE, DATETIME, DECIMAL(10,2), BINARY

SELECT CAST('123' AS UNSIGNED);
SELECT CAST(123 AS CHAR);
SELECT CAST('20220302' AS DATE);
```
