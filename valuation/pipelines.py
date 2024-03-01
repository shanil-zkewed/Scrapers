from datetime import date
from datetime import datetime
from datetime import timedelta

import re
import pymongo
from pymongo import MongoClient

from scrapy import settings
from scrapy.exceptions import DropItem

today1 = str(date.today())
yesterday = date.today()- timedelta(days = 1)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class ValuationPipeline1:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://zkewed:zkewed123A@vehicalevaluation.d9ufa.mongodb.net/?retryWrites=true&w=majority",
            27017
        )
        db = self.conn['data_store']
        self.collection = db['test_pipeline']

    def process_item(self, item, spider):
        if spider.name not in ['ikmancars','ikmanTest']: 
            return item
        
        p_date = item["date"]  
        temp_date = p_date[0].split(" ")[1] + " " + p_date[0].split(" ")[0] + " "  + str(date.today().year)
        temp_date1 = datetime.strptime(temp_date, '%b %d %Y')
        #final_date= datetime.strftime(temp_date1, '%m/%d/%Y')
        final_date= datetime.strftime(temp_date1, '%Y-%m-%d')
        #temp_date1 = datetime.datetime.strptime(temp_date1, format)
        price = item["price"]
        temp = price[0].split(" ")[1]
        
        item["url"] = item["url"][0]
        item["category"] = item["category"][0]
        item["make"] = item["make"][0]
        item["model"] = item["model"][0]
        item["year"] = item["year"][0]
        item["condition"] = item["condition"][0]
        item["price"] = temp
        item["mileage"] = item["mileage"][0]
        item["gear"] = item["gear"][0]
        item["fuel_type"] = item["fuel_type"][0]
        item["engine_capability"] = item["engine_capability"][0]
        item["location"] = item["location"][0]
        item["date"] = final_date
        item["scraped_date"] = today1
        item["store"] = "Ikman"

        '''if(date == str(yesterday)):
            self.collection.insert_one(dict(item))
            return item
        else:
            raise DropItem(f"missing price {item}")'''
            

        self.collection.insert_one(dict(item))
        return item
              
 

class ValuationPipeline2:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://zkewed:zkewed123A@vehicalevaluation.d9ufa.mongodb.net/?retryWrites=true&w=majority",
            27017
        )
        db = self.conn['data_store']
        self.collection = db['test_pipeline']

    def process_item(self, item, spider):
        if spider.name not in ['ikmanvans', 'ikmanbuses', 'ikman3wheeler', 'ikmanbikes','ikmanlorries']: 
            return item
        
        p_date = item["date"]  
        temp_date = p_date[0].split(" ")[1] + " " + p_date[0].split(" ")[0] + " "  + str(date.today().year)
        temp_date1 = datetime.strptime(temp_date, '%b %d %Y')
        final_date= datetime.strftime(temp_date1, '%Y-%m-%d')
        #temp_date1 = datetime.datetime.strptime(temp_date1, format)
        price = item["price"]
        temp = price[0].split(" ")[1]
        
        price = item["price"]
        temp = price[0].split(" ")[1]

        item["url"] = item["url"][0]
        item["category"] = item["category"][0]
        item["make"] = item["make"][0]
        item["model"] = item["model"][0]
        item["year"] = item["year"][0]
        item["price"] = temp
        item["mileage"] = item["mileage"][0]
        item["engine_capability"] = item["engine_capability"][0]
        item["location"] = item["location"][0]
        item["date"] = final_date
        item["scraped_date"] = today1
        item["store"] = "Ikman"            


        self.collection.insert_one(dict(item))
        return item


class ValuationPipeline3:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://zkewed:zkewed123A@vehicalevaluation.d9ufa.mongodb.net/?retryWrites=true&w=majority",
            27017
        )
        db = self.conn['data_store']
        self.collection = db['test_pipeline']

    def process_item(self, item, spider):
        if spider.name not in ['riya_cars','riya_suvs','riya_lorries','riya_3wheel',
                               'riya_bikes','riya_vans']: 
            return item
        
        category = item["category"]
        
        temp_category = category[0].split(" ")[-2]
        price = item["price"]
        temp = price[0].split(" ")[1]
        location = item["location"][0].split(", ")[-1]
        date1 = item["date"][0]
        #temp_date = re.search(r'\d{4}-\d{2}-\d{2}', date)
        temp_date = re.findall(r'\d{4}-\d{2}-\d{2}', date1)

        item["url"] = item["url"][0]
        item["make"] = item["make"][0]
        item["model"] = item["model"][0]
        item["year"] = item["year"][0]
        item["location"] = location
        item["engine_capability"] = item["engine_capability"][0] + str(" cc")
        item['category'] = temp_category
        item["gear"] = item["gear"][0]
        item["fuel_type"] = item["fuel_type"][0]
        item["mileage"] = item["mileage"][0]
        item["price"] = temp
        item["date"] = temp_date[0]
        #item["scraped_date"] = str(date.today().strftime('%m/%d/%y'))
        item["scraped_date"] = today1
        item["store"] = "Riyasewana"   

        '''if(date == str(yesterday)):
            self.collection.insert_one(dict(item))
            return item'''
                
        self.collection.insert_one(dict(item))
        return item
   

class ValuationPipeline4:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://zkewed:zkewed123A@vehicalevaluation.d9ufa.mongodb.net/?retryWrites=true&w=majority",
            27017
        )
        db = self.conn['data_store']
        self.collection = db['test_pipeline']


    def process_item(self, item, spider):
        if spider.name not in ['patpat']: 
            return item
        
        price = item["price"][0]
        #temp = price[0].split(" ")[1]
        #location = item["location"][0].split(", ")[-1]
        location = item["location"].split(", ")[-1]
        date1 = item["date"]
        #temp_date = re.search(r'\d{4}-\d{2}-\d{2}', date)
        temp_date = re.findall(r'\d{4}-\d{2}-\d{2}', date1)
        
        item["url"] = item["url"][0]
        item["location"] = location
        #item['category'] = item['category'][0].title()
        item['category'] = item['category'].title()
        item["date"] = temp_date[0]
        #item["scraped_date"] = str(date.today().strftime('%m/%d/%y'))
        item["scraped_date"] = today1
        item["store"] = "Patpat"   


        if(price == ":") or (price == " : Rs "):
            raise DropItem(f"missing price {item}")
        else:
            self.collection.insert_one(dict(item))
            return item
