-- List the number of records with the same score in table
SELECT DISTINCT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
