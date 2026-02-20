-- https://school.programmers.co.kr/learn/courses/30/lessons/131123

-- FOOD_TYPE별로 FAVORITES수가 가장 많은 식당의 FOOD_TYPE, REST_ID, REST_NAME, FAVORITES 조회
-- FOOD_TYPE 내림차순
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES)
                                    FROM REST_INFO
                                    GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC;
