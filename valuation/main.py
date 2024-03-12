import os
import schedule
import time
 
# running other file using run()

def task():
    os.system("scrapy crawl ikmanvans")
    os.system("scrapy crawl ikmancars")
    os.system("scrapy crawl riya_vans")
    os.system("scrapy crawl riya_suvs")
    os.system("scrapy crawl riya_cars")
    os.system("scrapy crawl patpat")
    print("done!")


schedule.every().day.at('09:10:00').do(task)

while True:
    schedule.run_pending()
    time.sleep(1)