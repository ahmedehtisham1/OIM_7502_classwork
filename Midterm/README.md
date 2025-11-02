# 🕸️ Introduction to Web Scraping with Scrapy (Python)

Welcome to the **Scrapy Intro** project, a guided, hands-on introduction to web scraping using the [Scrapy](https://scrapy.org) framework in Python.  
This repository accompanies a classroom tutorial that teaches how to:
- Create a Scrapy project
- Build and run a spider
- Handle pagination
- Export scraped data to CSV
- Analyze data with Pandas and Matplotlib

This project uses the demo website [Books to Scrape](https://books.toscrape.com), a safe sandbox for practicing scraping techniques.

---

##  Overview

**Scrapy** is a powerful open-source framework for extracting structured data from websites faster, cleaner, and more robust than ad-hoc `requests` + `BeautifulSoup` scripts.

Scrapy manages:
- **Requests** → sending efficient web requests.
- **Parsing** → extracting information with selectors.
- **Pipelines** → cleaning and storing data automatically.
- **Exporting** → saving data to CSV, JSON, XML, etc.
- **Concurrency** → crawling many pages at once.


---

##  Quick Start

### Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### Install Scrapy and Required Libraries

pip install scrapy pandas matplotlib seaborn


### Start a Scrapy Project

scrapy startproject bookdemo
cd bookdemo


### Create Your Spider

import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'rating': book.css('p.star-rating::attr(class)').get().split()[-1],
            }



