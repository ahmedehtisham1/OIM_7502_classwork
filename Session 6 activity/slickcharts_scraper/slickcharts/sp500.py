import scrapy

class Sp500Spider(scrapy.Spider):
    name = "sp500"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        
        rows = response.xpath('//table[contains(@class,"table")]/tbody/tr')
        for row in rows:
            number  = row.xpath('./td[1]/text()').get()
            company = row.xpath('./td[2]//a/text()').get()
            symbol  = row.xpath('./td[3]//a/text()').get()
            # YTD Return: 4th column normalize 
            ytd     = row.xpath('normalize-space(./td[4])').get()

    
            yield {
                "number": (number or "").strip(),
                "company": (company or "").strip(),
                "symbol": (symbol or "").strip(),
                "ytd_return": (ytd or "").strip(),
            }
