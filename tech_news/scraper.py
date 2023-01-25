import requests
from parsel import Selector
from time import sleep
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    return


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    all_links = selector.css(".entry-title a::attr(href)").getall()
    return all_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page = selector.css(".next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    data_news = {}
    data_news["title"] = selector.css(".entry-title::text").get().strip()
    data_news["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    data_news["writer"] = selector.css(".author a::text").get()
    data_news["timestamp"] = selector.css(".meta-date::text").get()
    comments_count = selector.css(".post-comments .title-block::text").get()

    data_news["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()

    data_news["comments_count"] = (
        int(comments_count.strip().split(" ")[0]) if comments_count else 0
    )

    post_tags = selector.css(".post-tags ul li a::text").getall()
    data_news["tags"] = post_tags if post_tags else []

    data_news["category"] = selector.css(
        ".entry-details span.label::text"
    ).get()

    return data_news


# Requisito 5
def get_tech_news(amount):
    url = fetch("https://blog.betrybe.com/")
    news = []

    while len(news) < amount:
        links_of_news = scrape_updates(url)
        for link in links_of_news:
            news.append(scrape_news(fetch(link)))
            if len(news) == amount:
                create_news(news)
                return news
        url_scraped = scrape_next_page_link(url)
        url = fetch(url_scraped)
