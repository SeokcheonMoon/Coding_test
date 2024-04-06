SELECT PRODUCT_CODE, PRICE*SUM(SALES_AMOUNT) AS SALES
FROM PRODUCT
INNER JOIN OFFLINE_SALE ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC
;