from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    new_list = []
    search_new = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in search_new:
        new_list.append((news["title"], news["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": date}}
        list_of_news = search_news(query)

        return [(news["title"], news["url"]) for news in list_of_news]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
