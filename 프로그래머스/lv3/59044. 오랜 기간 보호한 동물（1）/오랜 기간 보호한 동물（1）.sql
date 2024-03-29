SELECT NAME, DATETIME FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN 
(
    SELECT ANIMAL_INS.ANIMAL_ID FROM ANIMAL_INS
    INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
)
ORDER BY ANIMAL_INS.DATETIME LIMIT 3