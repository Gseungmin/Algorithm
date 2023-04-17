-- 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
-- FILE ID를 기준으로 내림차순
-- 조회수가 가장 높은 게시물은 하나만 존재
-- "/home/grep/src/" 게시글 ID를 기준으로 디렉토리가 구분
SELECT CONCAT("/home/grep/src/", BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT BOARD_ID FROM USED_GOODS_BOARD
ORDER BY VIEWS DESC
LIMIT 1)
ORDER BY FILE_ID DESC