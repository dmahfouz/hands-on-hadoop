# Performance benefit of Hive on Tez 

- In Ambari, on localhost:8080, navigate to Hive view
- If the Movielens names / ratings table is not in the `movielens` database, upload it using the following steps:
  - In the Hive view, click the "Upload Table" tab
  - For the "names" dataset, locate the `u.item` dataset in the `ml-100k` folder, set to pipe ( "|" ) delimited and set to the dataset name to "names"
  - Select `movielens` from the database dropdown
  - Set the first column names (`movie_id`, `name`, `release_date`) - the rest we don't need
  - Click "Upload Table"

- Using the MovieLens ratings dataset, type the following query in the query editor:

    ```sql
    DROP VIEW IF EXISTS topMovieIDs;

    CREATE VIEW topMovieIDs AS
    SELECT movie_id, count(movie_id) as ratingCount
    FROM movielens.ratings
    GROUP BY movie_id
    ORDER BY ratingCount DESC;

    -- create view that gets the top movie ids based on how many times
    -- the movie was rated and join it with the movie title database
    -- to display the names alongside the ratings counts


    SELECT n.name, ratingCount
    FROM topMovieIDs t JOIN movielens.names n ON t.movie_id = n.movie_id;
    ```

- To set the Hive execution engine to Tez:
  - In HDP Hive query editor, click on the settings cog in the right hand pane
  - Click on the green "add" button and in the left drop-down select `hive.execution.engine`
  - In the right drop-down, select `tez`
- Click the SQL tab in the right-hand pane, and then click "Execute" to execute the query
- In Tez, the query takes ~21 seconds

## Comparing the Tez vs. MapReduce Hive execution engines

- To run a Hive query with MapReduce as the execution engine, go back to the settings cog as before and select `mr` from the right dropdown
- Go back to the SQL view and click execute
- Running the same query with MapReduce in contrast takes ~1m11s, more than 3x the amount of time it took with Tez
- This illustrates a substantial performance gain with Tez compared to MapReduce