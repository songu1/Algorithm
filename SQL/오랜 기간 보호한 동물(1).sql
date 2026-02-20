-- https://school.programmers.co.kr/learn/courses/30/lessons/59044

-- ANIMAL_INS : 동물보호소 IN , ANIMAL_OUTS:동물보호소 OUT (입양)
-- 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문
-- 아직 입양을 못간 동물 ANIMAL_INS에 있지만 ANIMAL_OUTS에 없는 동물 
-- 가장 오래 보호소에 있었던 동물 : I.DATETIME이 오래된 순서
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY  I.DATETIME
LIMIT 3;
