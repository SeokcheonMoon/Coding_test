SELECT CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
LEFT JOIN CAR_RENTAL_COMPANY_CAR ON CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = CAR_RENTAL_COMPANY_CAR.CAR_ID
WHERE CAR_TYPE = '세단' and START_DATE LIKE '%2022-10%'
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
;