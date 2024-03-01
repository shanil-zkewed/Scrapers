import scrapy
from datetime import datetime
datetime.today().strftime('%Y-%m-%d')
from valuation.items import IkmanCarItem


class IkmanSpider(scrapy.Spider):
    name = "ikman3wheeler"
    allowed_domains = ["ikman.lk"]
    start_urls = ["https://ikman.lk/en/ads/sri-lanka/three-wheelers"]
    #start_urls = ["https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="+str(x) for x in range(1, 300)]

    def parse(self, response):
        #items = response.css('div.container--2uFyv')
        items = response.css('a.card-link--3ssYv.gtm-ad-item')

        for item in items:
            relative_url = item.css('a::attr(href)').get()
            yield response.follow(url=relative_url,callback=self.parse_veh_page)
        
        for i in range(1,170):
        #for i in range(1,2):
            next_page = "https://ikman.lk/en/ads/sri-lanka/three-wheelers?sort=date&order=desc&buy_now=0&urgent=0&page="+str(i)      
            #next_page = response.css('a[class*="col-6 lg-3 pag-next"] ::attr(href)').extract_first()
            if next_page is not None:
                #yield response.follow(next_page, callback=self.parse)
                yield scrapy.Request(url=next_page,callback=self.parse)
    
    def parse_veh_page(self, response):
        page = response.css('.left-section--PoAuT')

        carItem = IkmanCarItem()
        carItem["url"] = response.url,
        carItem["category"]= response.css('.link-text--1Tj-x::text')[3].get(),
        carItem["make"]= response.css('.ad-meta-desktop--1Zyra span::text')[0].get(),
        carItem["model"]= response.css('.ad-meta-desktop--1Zyra span::text')[1].get(),
           # "edition":
        carItem["year"]= response.css('.ad-meta-desktop--1Zyra span::text')[3].get(),
        carItem["condition"]=response.css('.ad-meta-desktop--1Zyra span::text')[2].get(),
        carItem["price"] = response.css('.amount--3NTpl::text').get(),
        carItem["mileage"] = response.css('.word-break--2nyVq.value--1lKHt::text')[1].get(),
        carItem["location"]= response.css('span.sub-title--37mkY span::text')[2].get(),
        carItem["date"]= response.css('.subtitle-wrapper--1M5Mv div::text')[2].get(),

        yield carItem

        """yield{
            "url": response.url,
            "category": response.css('.link-text--1Tj-x::text')[3].get(),
            "make": response.css('.ad-meta-desktop--1Zyra span::text')[0].get(),
            "model": response.css('.ad-meta-desktop--1Zyra span::text')[1].get(),
            "year":response.css('span::text')[13].get(),
            "price": response.css('.amount--3NTpl::text').get(), 
            'mileage': response.css('div.two-columns--19Hyo.full-width--XovDn.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-row--27fh1.flex--3fKk1 div.word-break--2nyVq.value--1lKHt::text')[1].get(),
            "condition": response.css('.ad-meta-desktop--1Zyra span::text')[2].get(),      
            "location": response.css('span.sub-title--37mkY span::text')[2].get(),
            "date": response.css('span.sub-title--37mkY::text')[2].get(),
            "options1": response.css('div.description--1nRbz p::text')[1].get(),
            #"options2": response.css('div.description--1nRbz p::text')[2].get(),
            #"options3":response.css('div.description--1nRbz p::text')[3].get()
            
        }"""
        