-- displays the top 3 of cities temp during july and agust
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
