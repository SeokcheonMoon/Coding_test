-- 코드를 입력하세요
SELECT ROUND(SUM(DAILY_FEE)/COUNT(CAR_TYPE),0) AS AVERAGE_FEE 
FROM CAR_RENTAL_COMPANY_CAR 
GROUP BY CAR_TYPE
HAVING CAR_TYPE='SUV'