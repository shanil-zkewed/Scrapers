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
        

    #os.system("scrapy crawl ikmanvans")
    #os.system("scrapy crawl ikmancars")
    #os.system("scrapy crawl riya_vans")
    #os.system("scrapy crawl riya_suvs")
    #os.system("scrapy crawl riya_cars")
    #os.system("scrapy crawl patpat")


    print("done!")


schedule.every().day.at('14:50:00').do(task)

while True:
    schedule.run_pending()
    time.sleep(1)

'''

from multiprocessing import Process, Queue
from valuation.spiders import patpat
from valuation.spiders import ikmanCars
from valuation.spiders import riyaSUV
from valuation.spiders import riyaCars
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def my_cloud_function(event, context):
    def script(queue):
        try:
            settings = get_project_settings()

            settings.setdict({
                'LOG_LEVEL': 'ERROR',
                'LOG_ENABLED': True,
            })

            process = CrawlerProcess(settings)
            process.crawl(patpat)
            process.crawl(ikmanCars)
            process.crawl(riyaCars)
            process.crawl(riyaSUV)
            process.start()
            print('start')
            queue.put(None)
        except Exception as e:
            queue.put(e)

    queue = Queue()

    # wrap the spider in a child process
    main_process = Process(target=script, args=(queue,))
    main_process.start()    # start the process
    main_process.join()     # block until the spider finishes

    result = queue.get()    # check the process did not return an error
    if result is not None:
        raise result 

    return 'ok'

'''