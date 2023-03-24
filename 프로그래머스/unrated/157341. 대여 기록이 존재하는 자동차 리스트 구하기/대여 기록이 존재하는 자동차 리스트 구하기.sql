-- 세단 자동차, 10월 대여, id 리스트 출력, id 중복 x
SELECT DISTINCT(CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID) From CAR_RENTAL_COMPANY_CAR
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY ON CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = CAR_RENTAL_COMPANY_CAR.CAR_ID
WHERE  MONTH(START_DATE) = 10 AND CAR_TYPE = "세단"
ORDER BY CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID DESC