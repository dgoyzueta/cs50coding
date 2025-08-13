--explain query plan
SELECT u.id
FROM users u
WHERE u.id IN (
    SELECT f.friend_id
    FROM friends f
    WHERE f.user_id = 284
    INTERSECT
    SELECT f.friend_id
    FROM friends f
    WHERE f.user_id = 440
);
