"""
main loop is here
"""
import schedule
import time
import datetime
from scripts.test import test_crawl

from scripts.test import elastic_csv

start_crawl_time="08"
end_crawl_time="15"
start_elastic_time="16"
end_elastic_time="17"
#def crawl_job():
 #   test_crawl.test_craw_indices()

#def elastic_job():
#    elastic_csv.elastic_csv()
#
#schedule.every().hour.at(":51").do(crawl_job)
#
#schedule.every().hour.at(":51").do(elastic_job)

last_hour="00"

while True:
    try:
        time_now=str(datetime.datetime.now().strftime("%H"))

        if start_crawl_time <= time_now <= end_crawl_time:
            while not last_hour == time_now:
                try:
                    test_crawl.save_indices_as_csv()
                except Exception as e:
                    print(e)
                    time.sleep(60)
                    continue
            
            last_hour=str(datetime.datetime.now().strftime("%H"))


        if start_elastic_time <= time_now <= end_elastic_time:
            while not last_hour == time_now:
                try:
                    elastic_csv.elastic_csv()
                
                except Exception as e:
                    print(e)
                    time.sleep(60)
                    continue

            last_hour=str(datetime.datetime.now().strftime("%H"))

        

        time.sleep(3600)
        
    except Exception as e:
        print(f"Exception in main loop line {e.__traceback__.tb_lineno}")
        print(e)
        time.sleep(10)