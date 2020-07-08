import praw
from psaw import PushshiftAPI
import pandas as pd
import time
import datetime as dt
import json 
# url = 'https://www.reddit.com/'
# with open('credentials.json') as f:
#     params = json.load(f)



# reddit = praw.Reddit(client_id=params['client_id'], 
#                      client_secret=params['api_key'],
#                      password=params['password'], 
#                      user_agent='<name it something descriptive> accessAPI:v0.0.1 (by /u/<yourusername>)',
                    #  username=params['username'])






import json 
  

with open('data//subreddits.json') as json_file: 
    data = json.load(json_file) 

subreddit_list=list(data.keys())


start_epoch=int(dt.datetime(2019, 4, 23).timestamp())

api = PushshiftAPI()
n_unique_commenters={}
unique_authors_subreddit={}
for index,subreddit in enumerate(subreddit_list):
    authors=[]

    gen =  api.search_comments(subreddit=f'{subreddit}',after=start_epoch)
    for x in gen:
        authors.append(x.author)
    authors=set(authors)
     
    n_unique_commenters[subreddit]=len(authors)
    unique_authors_subreddit[subreddit]=",".join(authors)
    print(f"Done with {subreddit}, {index} of {len(subreddit_list)}")
    time.sleep(1)




with open('data//unique_authors_list.json', 'w') as fp:
    json.dump(unique_authors_subreddit2, fp)
with open('data//n_unique_authors.json', 'w') as fp:
    json.dump(n_unique_commenters2, fp)
print("done")