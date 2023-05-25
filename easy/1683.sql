-- 1683. Invalid Tweets

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
