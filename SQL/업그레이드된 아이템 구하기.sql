-- https://school.programmers.co.kr/learn/courses/30/lessons/273711

-- ITEM_INFO : ITEM_ID , ITEM_NAME, RARITY(희귀도), PRICE
-- ITEM_TREE : ITEM_ID, PARENT_ITEM_ID
-- 각 ITEM_ID는 하나의 PARENT만 가짐, ROOT ITEM의 PARENT는 NULL
-- 업그레이드 : ROOT -> 아래 방향
-- RARITY가 'RARE'인 아이템의 모든 다음 업그레이드 아이템의 ITEM_ID, ITEM_NAME, RARITY 출력 (ITEM_ID DESC)

SELECT II.ITEM_ID, II.ITEM_NAME, II.RARITY
FROM ITEM_INFO II, ITEM_TREE IT
WHERE II.ITEM_ID = IT.ITEM_ID
AND IT.PARENT_ITEM_ID IN (SELECT I.ITEM_ID
                          FROM ITEM_INFO I
                          WHERE I.RARITY = 'RARE')
ORDER BY II.ITEM_ID DESC;
                        
