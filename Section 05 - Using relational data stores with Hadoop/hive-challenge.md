# Hive Challenge

## Find the movie with the highest average rating

- Hint: `AVG()` can be used on aggregated data, like COUNT() does
- Extra credit: only consider movies with more than 10 ratings

## Solution

```sql
DROP VIEW IF EXISTS averageMovieRatings;

CREATE VIEW IF NOT EXISTS averageMovieRatings AS 
SELECT movieID
  , COUNT(movieID) AS ratingCount
  , AVG(rating) AS avgRating
FROM ratings
GROUP BY movieID -- reduce operation
ORDER BY avgRating DESC;

SELECT n.title, t.avgRating, t.ratingCount
FROM topMovieIDs t JOIN names n ON t.movieID = n.movieID
WHERE t.ratingCount > 10;
```
