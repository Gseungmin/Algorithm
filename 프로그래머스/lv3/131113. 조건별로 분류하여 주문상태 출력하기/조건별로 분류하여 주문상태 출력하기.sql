-- 5월 1일 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부
-- 5월 1일 출고 완료로 이 후 날짜는 출고 대기 미정이면 출고 미정으로 출력
-- 주문 ID순 오름차순
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") AS OUT_DATE,
CASE
    WHEN DATE_FORMAT(OUT_DATE, "%Y-%m-%d") >"2022-05-01"
    THEN "출고대기"
    WHEN DATE_FORMAT(OUT_DATE, "%Y-%m-%d") <= "2022-05-01"
    THEN "출고완료"
    ELSE "출고미정"
    END
AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID