import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_alphavantage = 'KYMDUHPQ0JIUVLZI'

newsapi_key = "b872f0d2d1684125ac740da2b52f658b"

twilio_sid = "ACb91fa80f036c5ee2e25b60ced5b70871"
token = '9065fc9f95a37116d5f07b8a05e2f933'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_alphavantage = 'KYMDUHPQ0JIUVLZI'
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': api_alphavantage,
}

URL = 'https://www.alphavantage.co/query'
response = requests.get(url=URL, params=parameters)
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data['4. close']

print(yesterdays_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']

print(day_before_yesterday_closing_price)

difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((abs(difference) / float(yesterdays_closing_price)) * 100, 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


if diff_percentage > 5:
    news_url = 'https://newsapi.org/v2/everything'
    news_param = {
        'qInTitle': COMPANY_NAME,
        'language': 'en',
        'apiKey': newsapi_key
    }

    news = requests.get(url=news_url, params=news_param).json()
    print(news)
    three_news = news['articles'][:3]

    formated_articles = [f"{STOCK}: {up_down}{diff_percentage}%\n" \
                         f"Headline: {news['title']}\n" \
                         f"Brief: {news['description']}" for news in three_news]

    client = Client(twilio_sid, token)

    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_='+12543234708',
            to='+380995327348'
        )

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
