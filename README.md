<h1 align="center">
  <br>
  WallStreetBets Stock Scraper
  <br>
</h1>

<h4 align="center">A WallStreetBets stock scraper for the most recent talked about stocks.</h4>
<p align="center">
    <img src="https://user-images.githubusercontent.com/90940496/188292491-adc7abb3-38dc-4503-bf0f-d9ae7f0b7cfa.gif">
</p>

![wsbtrendingstocks](https://user-images.githubusercontent.com/90940496/188292503-81166aa2-3d2f-4216-80c7-6f6d81a83371.png)

## Description
Uses <a href="https://psaw.readthedocs.io/en/latest/">PSAW</a> to fetch posts from the wallstreetbets subreddit. </br>
Looks for stock tickers and checks if they are in the stocks dictionary created from <a href="https://www.nasdaq.com/market-activity/stocks/screener">Nasdaq's Stock Screener</a>. </br>
Uploads the valid stock tickers to the user's provided MongoDB database and collection.

## How To Use
User provides:
- MongoDB connection string
- Database name
- Collection name
- Number of recent posts to search




