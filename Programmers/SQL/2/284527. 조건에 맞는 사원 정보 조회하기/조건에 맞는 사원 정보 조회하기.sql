SELECT SUM(HR_GRADE.SCORE) AS SCORE, HR_GRADE.EMP_NO, HR_EMPLOYEES.EMP_NAME, HR_EMPLOYEES.POSITION, HR_EMPLOYEES.EMAIL
FROM HR_GRADE
INNER JOIN HR_EMPLOYEES ON HR_GRADE.EMP_NO = HR_EMPLOYEES.EMP_NO
GROUP BY HR_GRADE.EMP_NO
ORDER BY SCORE DESC
LIMIT 1