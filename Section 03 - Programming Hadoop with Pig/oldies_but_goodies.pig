ratings = LOAD '/user/maria_dev/ml-100k/u.data' 
    AS (
        userID:int, 
        movieID:int, 
        rating:int, 
        ratingTime:int
    );

metadata = LOAD '/user/maria_dev/ml-100k/u.item' USING PigStorage('|')
    AS (
        movieID:int, 
        movieTitle:chararray, 
        releaseDate: chararray, 
        videoRelease:chararray, 
        imdbLink:chararray
    );

nameLookup = FOREACH metadata 
    GENERATE 
        movieID, 
        movieTitle, 
        ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;

ratingsByMovie = GROUP ratings BY movieID;

avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID, AVG(ratings.rating) AS avgRating;

fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;

fiveStarsWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;

oldestFiveStarMovies = ORDER fiveStarsWithData BY nameLookup::releaseTime;

DUMP oldestFiveStarMovies;

-- -- debug
-- ratingsTopFive = LIMIT ratings 5; 
-- DESCRIBE ratings; 
-- DUMP ratingsTopFive;

-- metadataTopFive = LIMIT metadata 5; 
-- DESCRIBE metadata; 
-- DUMP metadataTopFive;

-- ratingsByMovieTopFive = LIMIT ratingsByMovie 5; 
-- DESCRIBE ratingsByMovie; 
-- DUMP ratingsByMovieTopFive;

-- avgRatingsTopFive = LIMIT avgRatings 5; 
-- DESCRIBE avgRatings; 
-- DUMP avgRatingsTopFive;

-- fiveStarMoviesTopFive = LIMIT fiveStarMovies 5; 
-- DESCRIBE fiveStarMovies; 
-- DUMP fiveStarMoviesTopFive;

-- fiveStarsWithDataTopFive = LIMIT fiveStarsWithData 5; 
-- DESCRIBE fiveStarsWithData; 
-- DUMP fiveStarsWithDataTopFive;

-- oldestFiveStarMoviesTopFive = LIMIT oldestFiveStarMovies 5; 
-- DESCRIBE oldestFiveStarMovies; 
-- DUMP oldestFiveStarMoviesTopFive;

