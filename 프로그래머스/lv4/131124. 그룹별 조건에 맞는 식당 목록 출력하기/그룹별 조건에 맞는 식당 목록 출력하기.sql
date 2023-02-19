-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL
-- 1. 리뷰를 가장 많이 작성한 회원 조회
-- 2. 해당 회원의 모든 리뷰 조회
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE FROM REST_REVIEW
INNER JOIN (SELECT T.MEMBER_ID, MEMBER_NAME FROM MEMBER_PROFILE
INNER JOIN (SELECT MEMBER_ID, COUNT(*) AS COUNTS FROM REST_REVIEW
GROUP BY MEMBER_ID
HAVING COUNTS = 
(SELECT COUNT(*) AS CNT FROM REST_REVIEW 
GROUP BY MEMBER_ID
ORDER BY CNT DESC
LIMIT 1)) AS T ON T.MEMBER_ID = MEMBER_PROFILE.MEMBER_ID) AS K ON K.MEMBER_ID = REST_REVIEW.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT