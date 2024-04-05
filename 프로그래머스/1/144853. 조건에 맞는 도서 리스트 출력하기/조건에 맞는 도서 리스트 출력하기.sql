-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHEDDATE
FROM BOOK 
WHERE PUBLISHED_DATE LIKE '%2021%' and CATEGORY='인문'
ORDER BY PUBLISHED_DATE ASC
;