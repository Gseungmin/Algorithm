SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH 
FROM MEMBER_PROFILE
WHERE GENDER = "W" AND TLNO != "NULL" 
AND DATE_FORMAT(DATE_OF_BIRTH,'%m') = '03'
ORDER BY MEMBER_ID