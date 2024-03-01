import scrapy
from valuation.items import RiyaCarItem

class RiyaSpider(scrapy.Spider):
    name = "riya_suvs"
    allowed_domains = ["riyasewana.com"]
    start_urls = ["https://riyasewana.com/search/suvs"]

    custom_settings = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

    def parse(self, response):
        items = response.css('div#content>ul>.item')
        for item in items:
            relative_url = item.css('h2.more>a::attr(href)').get()
            ##yield scrapy.Request(url=relative_url,callback=self.parse_veh_page)
            yield response.follow(url=relative_url,callback=self.parse_veh_page)

        #next_page = response.css('div.pagination>a:nth-last-child(2)::attr(href)').extract_first()
        next_page = response.css('div[id = "content"] div.pagination>a:nth-last-child(2)::attr(href)').extract_first()
        if next_page:
           next_page_url = response.urljoin(next_page)
           #next_page_url = next_page

        #uncomment this after testing
           yield scrapy.Request(url=next_page_url,callback=self.parse)

    def parse_veh_page(self, response):
 
        heading = response.css('div[id = "content"]')
        table_rows = response.css("table.moret tr")

        carItem = RiyaCarItem()

        carItem["url"] = response.url,
        carItem["category"] = heading.css("h1::text").get(),
        carItem["make"] = table_rows[4].css('td::text')[0].get(),
        carItem["model"] = table_rows[4].css('td::text')[1].get(),
        carItem["year"] = table_rows[5].css('td::text')[0].get(),
        carItem["price"] = table_rows[2].css('td span.moreph::text')[1].get(),
        carItem["mileage"] = table_rows[5].css('td::text')[1].get(),
        carItem["gear"]=table_rows[6].css('td::text')[0].get(),
        carItem["fuel_type"]= table_rows[6].css('td::text')[1].get(),
        carItem["engine_capability"] = table_rows[7].css('td::text')[1].get(),
        carItem["location"] = heading.css('h2::text').get(),
        carItem["date"] = heading.css("h2::text").get(),
        

        yield carItem


    ''' yield{
            "url" : response.url,
            "category":heading.css("h1::text").get(),
            "make" : table_rows[4].css('td::text')[0].get(),
            "model" : table_rows[4].css('td::text')[1].get(),
            "year": table_rows[5].css('td::text')[0].get(),
            "price":table_rows[2].css('td span.moreph::text')[1].get(),
            "mileage" : table_rows[5].css('td::text')[1].get(),
            "gear":table_rows[6].css('td::text')[0].get(),
            "fuel_type":table_rows[6].css('td::text')[1].get(),
            "engine_capability": table_rows[7].css('td::text')[1].get(),
            "location": heading.css('h2::text').get(),
            "date" :heading.css("h2::text").get(),
            "options": table_rows[7].css('td::text')[0].get()

        }'''
