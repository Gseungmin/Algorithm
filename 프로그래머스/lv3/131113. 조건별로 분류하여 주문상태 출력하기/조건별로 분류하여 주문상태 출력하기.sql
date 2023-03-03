-- 3:40
-- 5.1 까지 출고 완료는 출고 완료, 이 후 날짜는 출고 대기, 미정이면 출고 미정
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
CASE 
    WHEN OUT_DATE <= "2022-05-01" THEN "출고완료" 
    WHEN OUT_DATE > "2022-05-01" THEN "출고대기"
    ELSE "출고미정" 
    END AS 출고여부 
FROM FOOD_ORDER
ORDER BY ORDER_ID