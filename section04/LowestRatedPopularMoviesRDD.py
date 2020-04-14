import sys
from pyspark import SparkConf, SparkContext

def loadMovieNames():
	'''This function just creates a Python "dictionary" we can later
	use to convert movie ID's to movie names while printing out
	final results'''
	movieNames = {}
	with open("ml-100k/u.item") as f:
		for line in f:
			fields = line.split('|')
			movieNames[int(fields[0])] = fields[1]
	return movieNames

def parseInput(line):
	'''Take each line of u.data and convert it to (movieID, (rating, 1.0)).
	This way we can then add up all the ratings for each movie, and
	the total number of ratings for each movie (which lets us compute the average) '''
	fields = line.split()
	return (int(fields[1]), (float(fields[2]), 1.0))

def printTopNLines(dataset, n=10):
	topN = dataset.top(n)
	for row in topN:
		print(row)
	print("\n\n")

if __name__ == "__main__":

	if len(sys.argv) < 1:
		debug = False
	elif sys.argv[1].lower() == "true":
		debug = True
	elif sys.argv[1].lower() == "false":
		debug = False
	else:
		print("Accepted parameters: 'true' or 'false'")
		sys.exit(1)

	# The main script - create our SparkContext
	conf = SparkConf().setAppName("WorstPopularMovies")
	sc = SparkContext(conf = conf)

	# Load up our movie ID -> movie name lookup table
	movieNames = loadMovieNames()

	# Load up the raw u.data file
	lines = sc.textFile("hdfs:///user/maria_dev/ml-100k/u.data")
	
	# Convert to (movieID, (rating, 1.0))
	movieRatings = lines.map(parseInput)
	
	# Reduce to (movieID, (sumOfRatings, totalRatings))
	ratingsTotalAndCount = movieRatings.reduceByKey(
		lambda movie1, movie2: ( movie1[0] + movie2[0], movie1[1] + movie2[1] ))

	if debug: 
		# Debug
		print("Top 10 lines of dataset: `ratingsTotalAndCount`")
		printTopNLines(ratingsTotalAndCount)
	
	# Filter by totalRatings > 10
	popularRatingsTotalAndCount = ratingsTotalAndCount.filter(lambda x: x[1][1] > 10.0)

	if debug:	
		# Debug
		print("Top 10 lines of dataset: `popularRatingsTotalAndCount`")
		printTopNLines(popularRatingsTotalAndCount)

	# Map to (rating, averageRating)
	averageRatings = popularRatingsTotalAndCount.mapValues(
		lambda totalAndCount : (totalAndCount[0] / totalAndCount[1], totalAndCount[1] ))

	if debug:
		print("Top 10 lines of dataset: `averageRatings`")
		printTopNLines(averageRatings)

	# Flatten averageRatings inner tuple (each row is one tuple)
	averageRatingsFlattened = averageRatings.map(lambda row: (row[0], row[1][0], row[1][1]))
	
	if debug:
		print("Top 10 lines of dataset: `averageRatingsFlattened`")
		printTopNLines(averageRatingsFlattened)

	# Sort by lowest average rating and highest number of ratings
	sortedMovies = averageRatingsFlattened.sortBy(lambda x: x[1], ascending=True)

	sortedWorstPopularMovies = averageRatingsFlattened\
		.sortBy(lambda x: x[1], ascending=True)\
		.sortBy(lambda x: x[2], ascending=False)

	sortedPopularWorstMovies = averageRatingsFlattened\
		.sortBy(lambda x: x[2], ascending=False)\
		.sortBy(lambda x: x[1], ascending=True)
	
	if debug:
		print("Top 10 lines of dataset: `sortedMovies`")
		printTopNLines(sortedMovies)
		
		print("Top 10 lines of dataset: `sortedWorstPopularMovies`")
		printTopNLines(sortedWorstPopularMovies)

		print("Top 10 lines of dataset: `sortedPopularWorstMovies`")
		printTopNLines(sortedPopularWorstMovies)


	# Take the top 10 results
	results = sortedMovies.take(10)
	results2 = sortedWorstPopularMovies.take(10)
	results3 = sortedPopularWorstMovies.take(10)

	# Print them out:
	print("\n\nOriginal dataset - worst movies sorted by lowest average rating")
	print("="*75)
	for result in results:
		print(movieNames[result[0]], result[1], result[2])

	print("\n\nWorst movies sorted by lowest average rating and highest number of ratings")
	print("="*75)
	for result in results2:
		print(movieNames[result[0]], result[1], result[2])
	
	print("\n\nWorst movies sorted by highest number of ratings and lowest average rating")
	print("="*75)
	for result in results3:
		print(movieNames[result[0]], result[1], result[2])

