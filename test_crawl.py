
def save_indices_as_csv():
    import os
    import requests
    import jdatetime
    import pandas as pd

    try:
      
        url2 = "https://old.tsetmc.com/tsev2/data/MarketWatchPlus.aspx"
        data = requests.get(url2).text
        my_list = [line.split(',') for line in data.split(';')]

      
        df = pd.DataFrame(my_list[1:])
       # print("DataFrame created. Shape:", df.shape)

       
        output_dir = "E:/amir-ehsan/results/"
        #if not os.path.exists(output_dir):
        #    os.makedirs(output_dir)

        time_now = jdatetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
        output_path = os.path.join(output_dir, time_now)
        #print("Output path:", output_path)

       
        #if not df.empty:
        #    df.to_csv(output_path, index=False)
        #    print(f"File saved successfully at {output_path}")
        #else:
        #    print("DataFrame is empty. No file saved.")

    except Exception as e:
        print(f"Exception occurred: {e}")
   


if __name__=="__main__":
   save_indices_as_csv()

