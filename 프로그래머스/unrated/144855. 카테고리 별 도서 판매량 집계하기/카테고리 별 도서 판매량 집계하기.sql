SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES FROM BOOK_SALES
INNER JOIN BOOK ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = "2022-01"
GROUP BY CATEGORY
ORDER BY CATEGORY