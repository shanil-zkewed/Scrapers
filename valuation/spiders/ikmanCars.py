import scrapy
from datetime import datetime
from valuation.items import IkmanCarItem
datetime.today().strftime('%Y-%m-%d')


class IkmanCarSpider(scrapy.Spider):
    name = "ikmancars"
    allowed_domains = ["ikman.lk"]
    start_urls = ["https://ikman.lk/en/ads/sri-lanka/cars"]
    #start_urls = ["https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="+str(x) for x in range(1, 300)]

    def parse(self, response):
        #items = response.css('div.container--2uFyv')
        items = response.css('a.card-link--3ssYv.gtm-ad-item')

        for item in items:
            relative_url = item.css('a::attr(href)').get()
            yield response.follow(url=relative_url,callback=self.parse_veh_page)
        
        #for i in range(1,150):
        for i in range(1,15):
            next_page = "https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="+str(i)      
            #next_page = response.css('a[class*="col-6 lg-3 pag-next"] ::attr(href)').extract_first()
            if next_page is not None:
                #yield response.follow(next_page, callback=self.parse)
                yield scrapy.Request(url=next_page,callback=self.parse)
    
    def parse_veh_page(self, response):
        page = response.css('.left-section--PoAuT')

        
        carItem = IkmanCarItem()
        carItem["url"] = response.url,
        carItem["category"]= response.css('.link-text--1Tj-x::text')[3].get(),
        carItem["make"]=response.css('.ad-meta-desktop--1Zyra span::text')[0].get(),
        carItem["model"]=response.css('.ad-meta-desktop--1Zyra span::text')[1].get(),
           # "edition":
        carItem["year"]=response.css('.ad-meta-desktop--1Zyra span::text')[2].get(),
        carItem["condition"]=response.css('.ad-meta-desktop--1Zyra span::text')[3].get(),
        carItem["price"]= response.css('.amount--3NTpl::text').get(),
        carItem["mileage"]=response.css('.word-break--2nyVq.value--1lKHt::text')[3].get(),
        carItem["gear"]= response.css('.word-break--2nyVq.value--1lKHt::text')[1].get(),
           # "fuel_type":response.css('.word-break--2nyVq.value--1lKHt span::text')[5].get(),
        carItem["fuel_type"]=response.css('.ad-meta-desktop--1Zyra span::text')[5].get(),
        carItem["engine_capability"]= response.css('.word-break--2nyVq.value--1lKHt::text')[2].get(),
        carItem["location"]= response.css('span.sub-title--37mkY span::text')[2].get(),
        carItem["date"]= response.css('.subtitle-wrapper--1M5Mv div::text')[2].get(),
 
            
        yield carItem