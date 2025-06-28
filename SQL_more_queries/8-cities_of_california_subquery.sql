-- Cities of California
SELECT id, name
FROM Cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
