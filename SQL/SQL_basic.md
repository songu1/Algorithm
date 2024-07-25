# SQL 기본 문법

## 기본 쿼리
```sql
-- 결과 꺼내오기
SELECT <컬럼>
FROM <테이블명>
WHERE <조건>
-- 집계(꺼내온 결과로부터)
GROUP BY <그룹화할 컬럼>    -- 결과로부터 group by
HAVING <조건>              -- 그룹의 조건(특정 그룹만 보기)
ORDER BY <컬럼명> <ASC/DESC>;
```

## Table as Sets
#### DISTINCT : 중복을 제거해서 보여줌
```SQL
SELECT DISTINCT Salary FROM EMPLOYEE
```
#### 합집합 : UNION / UNION ALL
- UNION : 증복 데이터를 하나만 가져옴
- UNION ALL : 중복되는 데이터도 모두 가져옴
```SQL
SELECT name FROM customer
WHERE address LIKE '대한민국%'
UNION
SELECT name FROM customer
WHERE custid IN (SELECT custid FROM orders);
```

#### 교집합 : JOIN 사용
```SQL
SELECT A.str
FROM tableA A, tableB B
WHERE A.str = b.str;
```

#### 차집합 : not in
```sql
SELECT str FROM tableA WHERE str NOT IN (
    SELECT DISTINCT str FROM tableB
);
```

#### 대칭차집합
```sql
SELECT str FROM tableA WHERE str NOT IN (SELECT DISTINCT str FROM tableB)
UNION ALL
SELECT str FROM tableB WHERE str NOT IN (SELECT DISTINCT str FROM tableA);
```


## 기타 연산
### 서브문자열 패턴 매칭 LIKE
- % : 0개 이상의 문자
- _ : 문자 개수 지정
```SQL
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Address LIKE '%Houston, TX%';

SELECT Fname, Lname
FROM EMPLOYEE
WHERE Bdata LIKE '199_____-1______';
```

## 산술 연산
- +, - ,*
- BETWEEM a AND b : a이상 b이하

### NULL, EMPTY 체크
- NULL : 컬럼 IS NULL / IS NOT NULL
    - 값이 없는 경우
- EMPTY : 컬럼 = '' / 컬럼 != ''
    - 값이 비어있는 경우
```SQL
-- 컬럼에서 NULL 제외
SELECT * FROM BOARD
WHERE TITLE IS NOT NULL;

SELECT * FROM BOARD
WHERE TITLE != '';

SELECT * FROM BOARD
WHERE TITLE IS NULL OR TITLE=''
```


## 중첩쿼리
```SQL
-- Smith가 manager나 employee로 일하고 있는 프로젝트 번호를 중복 없이 검색하라
SELECT DISTINCT Pnumber FROM PROJECT
WHERE Pnumber IN
    (SELECT Pnumber FROM PROJECT, DEPARTMENT, EMPLOYEE
    WHERE Dnum = Dnumber AND Mgr_ssn = ssn AND Lname='Smith')
    OR
    Pnumber IN
    (SELECT Pno FROM WORKS_ON, EMPLOYEE
    WHERE Essn=ssn AND Lname='Smith');
```
### IN
- 집합 비교 연산자
- WHERE절
```SQL
SELECT DISTINCT ESSN FROM WORKS_ON
WHERE (Pno, Hours) IN (SELECT Pno, Hours
                        FROM WORKS_ON
                        WHERE ESSN='123456789');
```
### ALL
- single 값 비교 연산자
- WHERE절
- WHERE절에서 MAX, MIN 값 구하고 싶을 때 사용 가능
```sql
SELECT Lname, Fname
WHERE EMPLOYEE
WHERE Salary > ALL(SELECT Salary FROM EMPLOYEE WHERE Dno=5);
```

### (NOT)EXISTS : 수정하기!!!!*******************************************
- 상호연관 중첩쿼리의 결과가 empty인지 not empty인지 확인 => True/False를 반환
#### EXISTS
- 존재(TRUE) : 반환된 튜플에 해당하는 값 출력
- 존재X(FALSE) : 튜플 반환X (출력X)
```SQL
-- 부양가족을 갖는 매니저가 존재하면 EMPLOYEE 이름 출력
SELECT Fname, Lname FROM EMPLOYEE
WHERE EXISTS (SELECT * FROM DEPENDENT WHERE Ssn = Essn) -- EXISTS(부양가족) -> 부양가족
    AND EXISTS(SELECT * FROM DEPARTMENT WHERE Ssn=Mgr_ssn)  -- EXISTS(부서의 매니저)
```
#### NOT EXISTS
- 존재X : 모두가 반환되면 출력 X , 반환되지 않은 튜플이 있으며 해당하는 값 출력 
- 존재O : 반환된 튜플이 아예없으므로 모든 값 출력
```SQL

```


## JOIN

### JOIN
```SQL
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A JOIN 테이블명 B ON A.ID = B.ID;
```

### INNER JOIN 교집합
- 두 테이블의 공통된 내용을 뽑아내고 싶을 때
```SQL
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A INNER JOIN 테이블명 B ON A.ID=B.ID;
```

### LEFT JOIN
- ID값이 중첩될 경우 왼쪽 테이블의 ID값을 출력
#### LEFT에 있는것 전부 SELECT(공통 + LEFT)
```SQL
SELECT A.컬럼명
FROM 테이블명 A LEFT JOIN 테이블명 B ON A.ID = B.ID
```
#### LEFT에 있는것만(공통 제외)
```sql
SELECT A.컬럼명
FROM 테이블명 A LEFT JOIN 테이블명 B ON A.ID = B.ID
WHERE B.ID IS NULL;
```

### RIGHT JOIN
- ID값이 중첩될 경우 오른쪽 테이블의 ID값을 출력
#### RIGHT에 있는 것 전부 SELECT
```SQL
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A RIGHT JOIN B ON A.ID=B.ID;
```
#### RIGHT에 있는 것만(공통 제외)
```SQL
SELECT A.컬럼명, B.컬럼명
FROM 테이블명 A RIGHT JOIN 테이블명 B ON A.ID=B.ID
WHERE A.ID IS NULL;
```

## 집계함수
- COUNT, SUM, MAX, MIN, AVG, MEDIAN
    - 집계함수 : NULL값을 제외하고 구함
- DISTINCT : 열 중복 제외
- SELECT, HAVING절에서만 사용 가능
- GROUP BY절을 통해 그룹핑
- HAVING : 그룹을 SELECT

## GROUP BY
- grouping 하는 컬럼은 select절에서 반드시 나타나야함
- having : 어떤 그룹을 보여줄 것인가
- 그룹화하여 집계를 실행

## WITH 가상테이블
- 쿼리문이 실행될 때 임시로 사용하는 테이블
- SELECT로 가상 테이블 생성하기
```sql
WITH 가상테이블명 AS
(   -- 가상테이블을 만들고 싶은 SELECT문을 작성
    SELECT 컬럼A
    FROM 테이블명
    WHERE 조건
)
-- 가상테이블 사용
SELECT 컬럼A, 컬럼B
FROM 테이블명 B JOIN 가상테이블명 A ON A.ID=B.ID
WHERE 조건;
```