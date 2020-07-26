#!usr/bin/python36

import os
from pprint import pprint
from starbase import Connection

c = Connection("127.0.0.1", "8000")

print("Printing tables (checking connection)\n")
print(c.tables())

ratings = c.table('ratings')

if (ratings.exists()):
    print("Dropping existing ratings table\n")
    ratings.drop()

ratings.create('rating')

print("Checking file exists...\n")
filePath = "C:/Users/davidm/Downloads/ml-100k/ml-100k/u.data"
print(os.path.exists(filePath))


print("Parsing the ml-100k ratings data...")
ratingFile = open("C:/Users/davidm/Downloads/ml-100k/ml-100k/u.data", "r")

batch = ratings.batch()

print("Updating data...\n")
for i, line in enumerate(ratingFile):
    # if i % 1000 == 0:
    #     print(line)

    (userID, movieID, rating, timestamp) = line.split()
    batch.update(userID, {'rating': {movieID: rating }})

    # if (userID == "1") or (userID == "33"):
    #     print(line)

ratingFile.close()

print("Committing ratings data to HBase via REST service\n")
batch.commit(finalize=True)

# print(ratings)
print("\n====== PRINTING TABLE SCHEMA ========....\n")
print(ratings.schema())

print("\n====== PRINT ALL TABLE ROWS =========....\n")
print(ratings.fetch_all_rows())


print("\nGetting back ratings for some users...\n")

print("Ratings for user ID 1:\n")
pprint(ratings.fetch("1"), indent=4)

print("\nRatings for user ID 33:\n")
pprint(ratings.fetch("33"), indent=4)
