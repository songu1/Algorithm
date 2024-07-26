-- 그룹별 조건에 맞는 식당 목록 출력하기
-- 프로그래머스 오라클 Lv4

WITH MEMBER_REVIEW AS
(
    SELECT A.MEMBER_ID AS MEMBER_ID, MEMBER_NAME, COUNT(*) AS COUNT
    FROM MEMBER_PROFILE A, REST_REVIEW B
    WHERE A.MEMBER_ID=B.MEMBER_ID
    GROUP BY A.MEMBER_ID, MEMBER_NAME
)
SELECT MEMBER_NAME, REVIEW_TEXT, TO_CHAR(REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE
FROM REST_REVIEW R INNER JOIN MEMBER_REVIEW M ON R.MEMBER_ID = M.MEMBER_ID
WHERE COUNT = (SELECT MAX(COUNT)
              FROM MEMBER_REVIEW)
ORDER BY REVIEW_DATE, REVIEW_TEXT


-- with를 사용하여 조회 결과를 임시테이블로 생성 후 문제 해결!

-- MYSQL
WITH MEMBER_VIEW AS
(
    SELECT M.MEMBER_ID, M.MEMBER_NAME, COUNT(*) AS COUNT
    FROM MEMBER_PROFILE M, REST_REVIEW R
    WHERE M.MEMBER_ID = R.MEMBER_ID
    GROUP BY MEMBER_ID, MEMBER_NAME
)
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_VIEW M, REST_REVIEW R
WHERE M.MEMBER_ID = R.MEMBER_ID
    AND M.COUNT = (SELECT MAX(COUNT) FROM MEMBER_VIEW)
ORDER BY REVIEW_DATE, REVIEW_TEXT;
