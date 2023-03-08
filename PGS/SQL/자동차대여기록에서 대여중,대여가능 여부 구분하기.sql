-- 자동차 대여기록에서 대여중/대여가능 여부 구분하기
-- 프로그래머스 lv3

-- CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- HISTORY_ID(자동차 대여기록ID) CAR_ID(자동차ID) START_DATE(대여시작일), END_DATE(대여종료일)

-- 2022년 10월 16일에 대여 중인 자동차는 '대여중',대여 중이지 않은 자동차는 '대여 가능'
-- 을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가하여 동차 ID와 AVAILABILITY 리스트를 출력
-- 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬

-- START_DATE가 2022/10/16 이하, END_DATE가 2022/10/16이상

SELECT DISTINCT CAR_ID,
    MAX(CASE WHEN START_DATE<=TO_DATE('2022-10-16','YYYY-MM-DD')
    AND END_DATE>=TO_DATE('2022-10-16','YYYY-MM-DD') THEN '대여중'
    ELSE '대여 가능' END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;

-- 문자열 max ***
-- max : 대여중이 대여 가능보다 크게 나옴