import os
import schedule
import time
import requests
 
# running other file using run()

def task():
 
    while True:
        try:
            os.system("scrapy crawl ikmanvans")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)

        try:
            os.system("scrapy crawl ikmancars")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)

        try:
            os.system("scrapy crawl riya_vans")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)

        try:
            os.system("scrapy crawl riya_suvs")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)
        
        
        try:
            os.system("scrapy crawl riya_cars")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)
        
        try:
            os.system("scrapy crawl patpat")
            break
        except (requests.exceptions.ConnectionError, FileNotFoundError):
            print("error, trying again in 10s")
            time.sleep(5)
        

    '''  
    os.system("scrapy crawl ikmanvans")
    os.system("scrapy crawl ikmancars")
    os.system("scrapy crawl riya_vans")
    os.system("scrapy crawl riya_suvs")
    os.system("scrapy crawl riya_cars")
    os.system("scrapy crawl patpat")


    print("done!")
    '''

schedule.every().day.at('07:50:00').do(task)

while True:
    schedule.run_pending()
    time.sleep(1)