-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID)
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR > 8 AND HOUR < 20
ORDER BY HOUR;