-- https://school.programmers.co.kr/learn/courses/30/lessons/298519

-- 평균 LENGTH가 33cm 이상인 물고기를 종류별 분류 -> count, max length, type 출력 (type asc 정렬)
-- 10cm 이하 물고기는 10cm로 취급
-- FISH_TYPE, FISH_COUNT, MAX_LENGTH

SELECT COUNT(FI.ID) AS FISH_COUNT, MAX(FI.LENGTH) AS MAX_LENGTH, FI.FISH_TYPE
FROM (SELECT ID, FISH_TYPE, IFNULL(LENGTH,10) AS LENGTH FROM FISH_INFO) AS FI
GROUP BY FI.FISH_TYPE
HAVING AVG(FI.LENGTH) >= 33
ORDER BY FISH_TYPE;
