#bismillah
import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
from twilio.rest import Client

STOCK_API_KEY = "922NTRF99YW2UPL1"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "92208d27f5bb420cb1f87f3be1436236"

    ## STEP 1: Use
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    #https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
#Getting yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={STOCK_API_KEY}")
var = response.json()
# print(var)

yesterday = var["Time Series (5min)"]["2023-07-11 19:55:00"]["4. close"]
# print(yesterday)

#- Get the day before yesterday's closing stock price
dayBeforeYesterday= var["Time Series (5min)"]["2023-07-11 18:55:00"]["4. close"]
# print(dayBeforeYesterday)
five = var["Time Series (5min)"]["2023-07-11 17:50:00"]["4. close"]
#. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday))-float(dayBeforeYesterday)

diff_percentage = (difference/float(yesterday))*100
# print(diff_percentage)

#. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.




#. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percentage>0.01:
    # print("Get News")
    news_params={
        "apiKey":NEWS_API,
        "qInTitle":COMPANY_NAME,
    }
    RESPONSE = requests.get(NEWS_ENDPOINT,params=news_params)
    # print(RESPONSE.json())

    articles = RESPONSE.json()["articles"]
    # print(articles)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
threeArticles = articles[:3]
# print(threeArticles)
formatted = [f"Headline: {article['title']}.\nBrief: {article['description']}"  for article in threeArticles]
print(formatted)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#. - Create a new list of the first 3 article's headline and description using list comprehension.

# - Send each article as a separate message via Twilio.

account_sid = 'AC0a955c1d38dde0fdc4ecdd7582aa351e'
auth_token = '2b014579fdb7851882f9d98f17fb7849'
client = Client(account_sid, auth_token)

for article in formatted:
    message = client.messages.create(
      from_='+12342782334',
      to='+918792549715',
      body=article+"\n\n\n Alhamdulillah"
    )

print(message.sid)


