
SELECT CAR_ID, if(sum(if(date_format(START_DATE, "%Y-%m-%d") > '2022-10-16' 
        OR  date_format(END_DATE, "%Y-%m-%d") < '2022-10-16', 0, 1)) > 0, "대여중", "대여 가능")
        AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC