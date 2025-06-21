import os
import praw
from dotenv import load_dotenv

load_dotenv()
def fetch_reddit_data(topic, limit=10):
    try:
        reddit=praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),client_secret=os.getenv('REDDIT_CLIENT_SECRET'),user_agent=os.getenv('REDDIT_USER_AGENT'))
        reddit.read_only=True  #giving the read only permission we cannot modify

        #fetch posts for reddit in read only
        posts=[]
        subreddit=reddit.subreddit('all') #it will fetch all the important keys or subreddit
        for submission in subreddit.search(topic, sort='new',time_filter='all',limit=limit):
            posts.append({
                "title": submission.title,
                "content":submission.selftext or'No content available', #subtext retrieve the texts from content, if there is no content then it will give a message that there is no any content available
                "url": submission.url
            })
        return posts 

    except Exception as e:
        print(f'Error fetching data from reddit : {e}')
        return []
