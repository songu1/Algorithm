-- 주문량이 많은 아이스크림들 조회하기
-- 프로그래머스 LV4

-- FIRST_HALF 아이스크림 가게의 상반기 주문 정보
-- SHIPMENT_ID(출하번호) FLAVOR(아이스크림 맛) TOTAL_ORDER(상반기 아이스크림 총주문량)
    -- 기본키 : FLAVOR / 외래키 : SHIPMENT_ID (JULY의 SHIPMENT_ID의 외래키)
-- JULY 7월의 아이스크림 주문정보를 담은 JULY 테이블
-- SHIPMENT_ID(출하번호) FLAVOR(맛) TOTAL_ORDER(7월의 아이스크림 총주문량)
    -- 기본키 : SHIPMEMT_ID / 외래키 : FLAVOR (FIRST_HALF의 FLAVOR의 외래키)

-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로
-- 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.
    
SELECT FLAVOR
FROM (SELECT F.FLAVOR, F.TOTAL_ORDER+A.TOTAL_ORDER AS TOTAL_ORDER
      FROM FIRST_HALF F, (SELECT J.FLAVOR, SUM(J.TOTAL_ORDER) AS TOTAL_ORDER
                          FROM JULY J
                          GROUP BY J.FLAVOR) A 
      WHERE F.FLAVOR=A.FLAVOR
      ORDER BY TOTAL_ORDER DESC)
WHERE ROWNUM<=3;


-- FIRST_HALF의 맛 별 TOTAL_ORDER + JULY의 (GROUP BY FLAVOR)한 값의 맛 별 TOTAL_ORDER

-- 3중 쿼리 사용
-- 1번쿼리 : 상위3개의 값을 조회하기 위한 쿼리 - WHERE ROWNUM 사용
-- 2번쿼리 : FIRST_HALF와 JULY테이블의 맛 별 TOTAL_ORDER 값을 더해주기위한 쿼리 - SELECT절에서 +로 합쳐줌
-- 3번쿼리 : JULY 테이블에서 맛 별 TOTAL_ORDER를 구해주기위한 쿼리 - GROUP BY FLAVOR