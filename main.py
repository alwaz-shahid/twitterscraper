import os
import pandas as pd
from datetime import datetime, timedelta

# today = datetime.today().strftime('%Y-%m-%d')
today = datetime.today()
end_date = today
startdate = today - timedelta(days=30)

print(startdate)
search_term = 'bitcoin'
os.system(f"snscrape --since {startdate} twitter-search '{search_term} until:{end_date}' > {search_term}.txt")
if os.path.exists(f"{search_term}.json"):
    df = pd.read_json(f"{search_term}.json", lines=True)
    df.to_csv(f"{search_term}.csv", index=False)
    print(f"{search_term}.csv created successfully")
else:
    print("No data found")
if os.stat(f"{search_term}.json").st_size == 0:
    print("File is empty")
    count = 0
else:
    df=pd.read_csv(f"{search_term}.txt", sep=";", header=None,names=['link'])
    # df=pd.read_json(f"{search_term}.json", lines=True)
    # d
    count = df.size
    print("File is not empty")

print("Total tweets: ", count)
# search_term = search_term.replace(' ', '+')
# url = f'https://www.google.com/search?q={search_term}&tbs=cdr:1,cd_min:{startdate},cd_max:{end_date}&tbm=nws'
# print(url)
# start_date= startdate.strftime('%Y-%m-%d')
# search_query = 'from:elonmusk until:2020-10-01 since:2020-09-01'
