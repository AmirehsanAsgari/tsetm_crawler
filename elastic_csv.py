
def shamsi_to_epoch(data_file):
    import jdatetime
    import time
    import datetime
    year,month,day,hour=map(int,data_file.split('-'))
    gregorin_date = jdatetime.date(year,month,day).togregorian()
    gregorin_date=int(gregorin_date.strftime("%Y%m%d"))
    #total_time=int(str(gegorin_date) + str(hour))
    total_time_to_datetime=datetime.datetime.strptime(str(gregorin_date)+str(hour),"%Y%m%d%H")
    epoch_time=int(time.mktime(total_time_to_datetime.timetuple()))
    return epoch_time       





def data_generator(reader_file,data_file_for_epoch):
    for row in reader_file:
        yield {
            "id":row[1],
            "code":row[2],
            "symbol":row[3],
            "name":row[4],
            "open":row[6],
            "close":row[7],
            "volume":row[10],
            "price":row[11],
            "low":row[12],
            "high":row[13],
            "epech":shamsi_to_epoch(data_file_for_epoch)

            
        }
             
def etl_csv_to_elastic():
    import pandas as pd     
    from elasticsearch import Elasticsearch,helpers
    import csv
    from datetime import datetime
    es=Elasticsearch("http://127.0.0.1:9200")
    now=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    year,month,day,hour,Minute,Second=map(int,now.split('-'))
       
    for i in range(day):
            for j in range(8,15):
                try:
                    data_file=f"E:/amir-ehsan/results/1403-{month:02d}-{i:02d}-{j:02d}.csv"
                    data_file_for_epoch=data_file.split(".")[0]    
                    with open(data_file,"r", encoding="utf-8") as file_r:   
                            reader_file=csv.reader(file_r)   
                            helpers.bulk(es,data_generator(reader_file,data_file_for_epoch), index='tmstse')
                    

                except Exception as e:
                    print(f"errors file{data_file}")
                    continue   
