-- 3:47
-- 들어올때 중성화 X 나갈때 중성화 O
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.ANIMAL_TYPE, ANIMAL_OUTS.NAME FROM ANIMAL_INS
INNER JOIN ANIMAL_OUTS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE (SEX_UPON_INTAKE NOT LIKE "%Spayed%" AND SEX_UPON_INTAKE NOT LIKE "%Neutered%")
    AND (SEX_UPON_OUTCOME LIKE "%Spayed%" OR SEX_UPON_OUTCOME LIKE "%Neutered%")
ORDER BY ANIMAL_OUTS.ANIMAL_ID
