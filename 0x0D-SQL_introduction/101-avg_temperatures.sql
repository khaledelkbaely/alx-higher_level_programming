-- displays the average temperature
SELECT city, AVG(value) AS avg_temps
FROM temperatures
GROUP BY city
ORDER BY avg_temps DESC;
