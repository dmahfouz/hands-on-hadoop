# Pig Challenge: find the most popular bad movies

## Defining the problem

- Find all the movies with an average rating less than 2.0 stars
- Sort them by the total number of ratings

## Hint

- Everything you need is in the example of finding movies with ratings > 4.0 (`oldies_but_goodies.pig`)
- Only new thing you need is `COUNT()`, that let's you count the number of items in a bag
  - Just like you can say `AVG(ratings.rating)` to get an average rating from a bag of ratings
  - You can do `COUNT(ratings.rating)` to get the total number of ratings for a given group's bag
