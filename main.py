import os
from scraper import Scraper
from cleaner import Cleaner
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
scraper = Scraper(bearer_token=bearer_token, target_username='CNN')

newer_tweet = scraper.get_newer_tweet()
replies = scraper.get_replies(newer_tweet)
scraper.save_as_files(newer_tweet, replies)

cleaner = Cleaner()
cleaner.clean_all_replies()
