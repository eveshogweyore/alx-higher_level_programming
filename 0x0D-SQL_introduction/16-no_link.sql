-- List all records of table `second_table` with certain criteria.
SELECT score, name
FROM  name second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
