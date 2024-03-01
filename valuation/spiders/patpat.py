from urllib import response
import scrapy
from valuation.items import RiyaCarItem


class PatpatSpider(scrapy.Spider):
    name = "patpat"
    allowed_domains = ["patpat.lk"]
    start_urls = ["https://www.patpat.lk/vehicle"]
    #start_urls = ["https://www.patpat.lk/vehicle?page="+str(x) for x in range(1, 51)]

    def parse(self, response):
        items = response.css('div.result-data.col-lg-9.pr-lg-0')
        for item in items:
            relative_url = item.css('a').attrib['href']
            yield response.follow(url=relative_url,callback=self.parse_veh_page)
    
        #next_page_url = response.css('ul.pagination.pagination.li.nth-last-child(2)::attr(href)').extract_first()
        next_page_url = response.css('.pagination>li:last-child>a::attr(href)').extract_first()
        if next_page_url:
          next_page_url = response.urljoin(next_page_url)
          # uncomment line below after testing
          yield scrapy.Request(url=next_page_url,callback=self.parse)

    def parse_veh_page(self, response):
        page = response.css('.holder.container.item-preview')
        res = response.css('div.info-inner')
        table_rows = response.css("table.course-info.table.table-striped tr")
        overview = response.css('div.item-description.card.mt-3.mb-3.p-3')

        carItem = RiyaCarItem()

        carItem["url"] =  response.url,
        carItem["category"] = page.css('li.breadcrumb-item a::text')[2].get()
        carItem["make"] = table_rows[4].css('td::text')[1].get()
        carItem["model"] = table_rows[5].css('td::text')[1].get()
        carItem["year"] = table_rows[1].css('td::text')[1].get()
        carItem["price"] = res.css('span::text')[1].get()
        carItem["mileage"] = table_rows[8].css('td::text')[1].get()
        carItem["gear"] = table_rows[3].css('td::text')[1].get()
        carItem["fuel_type"] = table_rows[6].css('td::text')[1].get()
        carItem["engine_capability"] = table_rows[7].css('td::text')[1].get()
        carItem["location"] = page.css('p.intro-line.col-12::text').get()
        carItem["date"] = page.css('p.intro-line.col-12::text').get()

        yield carItem

        '''
        yield{
            "url": response.url,
            "category":page.css('li.breadcrumb-item a::text')[2].get(),
            "make": table_rows[4].css('td::text')[1].get(),
            "model":table_rows[5].css('td::text')[1].get(),
            "year":table_rows[1].css('td::text')[1].get(),
            "price": res.css('span::text')[1].get(),
            "mileage": table_rows[8].css('td::text')[1].get(),
            "gear":table_rows[3].css('td::text')[1].get(),
            "fuel_type": table_rows[6].css('td::text')[1].get(),
            "engine_capacity":table_rows[7].css('td::text')[1].get(),
            "location": overview.css('p::text').get(),
            "date":page.css('p.intro-line.col-12::text').get(),
        }
        '''