-- 코드를 입력하세요
-- BOOK, AUTHOR : AUTHOR_ID
-- BOOK, BOOK_SALES : BOOK_ID

-- BOOK_ID, CATEGORY, AUTHOR_ID, PRICE, PUBLISHED_DATE
-- AUTHOR_ID, AUTHOR_NAME
-- BOOK_ID, SALES_DATE, SALES

WITH EMP_SALES AS(
SELECT BOOK_ID, SUM(SALES) AS SALES
FROM BOOK_SALES
WHERE EXTRACT(YEAR FROM SALES_DATE)=2022 AND EXTRACT(MONTH FROM SALES_DATE)=1
GROUP BY BOOK_ID
)
SELECT B.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) AS TOTAL_SALES
FROM BOOK B, AUTHOR A, EMP_SALES E
WHERE B.BOOK_ID=E.BOOK_ID AND B.AUTHOR_ID=A.AUTHOR_ID
GROUP BY B.AUTHOR_ID, AUTHOR_NAME, CATEGORY
ORDER BY B.AUTHOR_ID ASC, CATEGORY DESC;

-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 
-- 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여,
-- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.

