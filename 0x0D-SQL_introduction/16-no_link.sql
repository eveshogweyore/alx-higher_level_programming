-- List all records of table `second_table` with certain criteria.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) <> '';
