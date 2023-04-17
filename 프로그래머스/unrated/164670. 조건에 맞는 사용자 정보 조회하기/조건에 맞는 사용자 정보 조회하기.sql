-- 9:24
-- 중고 거래 게시물을 3건 이상 등록한 사용자
-- 사용자의 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL 작성
-- 시 도로명 상세주소가 함께
-- 전화번호는 하이픈 삽입하여 출력
-- 회원 ID를 기준으로 내림차순 정렬
SELECT USER_ID, NICKNAME, CONCAT(CITY, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2) AS "전체주소",
CONCAT(LEFT(TLNO, 3), "-", SUBSTRING(TLNO, 4, 4) ,"-", RIGHT(TLNO, 4)) AS "전화번호"
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT WRITER_ID FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING COUNT(*) >= 3)
ORDER BY USER_ID DESC