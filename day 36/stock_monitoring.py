import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "="
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": "="
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
today_date = stock_data["Meta Data"]["3. Last Refreshed"]
today_date_obj = datetime.strptime(today_date, "%Y-%m-%d")
yesterday_date_obj = today_date_obj - timedelta(days=1)
day_before_yesterday_date_obj = today_date_obj - timedelta(days=2)
yesterday_date_str = yesterday_date_obj.strftime("%Y-%m-%d")
day_before_yesterday_date_str = day_before_yesterday_date_obj.strftime("%Y-%m-%d")
yesterday_closing_price = stock_data["Time Series (Daily)"][yesterday_date_str]["4. close"]
day_before_yesterday_closing_price = stock_data["Time Series (Daily)"][day_before_yesterday_date_str]["4. close"]
print(f"Closing price for {yesterday_date_str}: {yesterday_closing_price}")
print(f"Closing price for {day_before_yesterday_date_str}: {day_before_yesterday_closing_price}")
converted_yesterday_closing_price = float(yesterday_closing_price)
converted_day_before_yesterday_closing_price = float(day_before_yesterday_closing_price)
difference_in_closing_price = abs(converted_yesterday_closing_price - converted_day_before_yesterday_closing_price)
print(difference_in_closing_price)
difference_in_percentage = 0.05 * float(yesterday_closing_price)
print(difference_in_percentage)
if difference_in_closing_price >= difference_in_percentage:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    article_list = []
    for article in news_data['articles'][:3]:
        headline = article["title"]
        description = article["description"]
        article_list.append({'headline': headline, 'description': description})
    print(article_list)
else:
    print("no big change")
