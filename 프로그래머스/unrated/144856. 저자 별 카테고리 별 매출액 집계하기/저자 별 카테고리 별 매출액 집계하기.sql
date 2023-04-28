-- 9:58
-- 22년 1월 저자별 카테고리별 매출액
-- 저자 ID, 저자 명, 카테고리 매출액을 리스트로 출력
-- 저자 ID 오름차순, 카테고리 내림차순
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM (SELECT book_id, category, BOOK.author_id, price, published_date, author_name FROM BOOK
INNER JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID) AS T
INNER JOIN BOOK_SALES ON T.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE DATE_FORMAT(sales_date, "%Y-%m") = "2022-01"
GROUP BY author_id, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC