from psaw import PushshiftAPI
import pymongo
from pymongo import MongoClient
from csv import DictReader

connectionString = input("Enter your connection string: ")
dbName = input("Enter database name: ")
collectionName = input("Enter collection name: ")
limitNum = int(input("Enter limit: "))

cluster = MongoClient(connectionString)
db = cluster[dbName]
collection = db[collectionName]

# create stocks dictionary
file_handle = open("nasdaq_screener.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)
stocks = {}
for row in csv_reader:
    stocks[row["Symbol"]] = [row["Name"], row["Sector"], row["Industry"]]

api = PushshiftAPI()

submissions = api.search_submissions(subreddit='wallstreetbets', filter=[
    'url', 'author', 'title', 'subreddit'], limit=limitNum)

for submission in submissions:

    words = submission.title.split()
    cashtags = list(
        set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        for cashtag in cashtags:
            # check if theres a non char at the end of the tag, if so remove it
            if (not cashtag[len(cashtag)-1].isalpha()):
                ticker = cashtag[:-1]
            else:
                ticker = cashtag[1:]

            if (ticker in stocks):
                post = {"Ticker": ticker, "Name": stocks[ticker][0], "Sector": stocks[ticker][1], "Industry": stocks[ticker][2], "Post Title": submission.title,
                        "Post Url": submission.url}
                print(post)
                collection.insert_one(post)
