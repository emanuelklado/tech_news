from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    new_list = []
    search_new = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in search_new:
        new_list.append((news["title"], news["url"]))
    return new_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
