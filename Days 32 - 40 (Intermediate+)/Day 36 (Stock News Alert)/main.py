import requests
from newsapi import NewsApiClient
from time import sleep

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

Alpha_van_KEY = '3ZB9J5P2BV47N5MK'

news_KEY = '7ca64f9c84f7438cb6f168255633d99d'
newsapi = NewsApiClient(api_key=news_KEY)


def get_news():
    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                          sources='bbc-news,the-verge',
                                          from_param='2022-11-12',
                                          to='2022-12-31',
                                          language='en',
                                          sort_by='relevancy')
    news_data = {}
    num = 0
    for i in all_articles['articles']:
        news_data[i['title']] = i['url']
        num += 1

    with open("news.txt", "w") as file:
        for key, val in news_data.items():
            file.write(f"{key} : {val}\n")


def get_stock():
    my_list = []
    api = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={Alpha_van_KEY}"
    response = requests.get(api)
    data = response.json()

    num = 0
    for i in data["Time Series (60min)"]:
        my_list.append(data["Time Series (60min)"][i]["4. close"])
        num += 1
        if num == 24:
            break
    comparison_new = float(my_list[0])
    comparison_old = float(my_list[-1])

    percentage = comparison_new * 0.05
    validator = comparison_old + percentage

    if validator <= comparison_new:
        print("getting news")
        get_news()


while True:
    get_stock()
    sleep(600)
