SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS 'COUNT' FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR