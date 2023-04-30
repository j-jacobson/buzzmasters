#!/usr/bin/env python3
from decouple import config
from datetime import datetime
from pathlib import Path, PurePath
import sys
import time
import praw
import openai
import random
from bot_helper import get_bots, login, HOURLY_COMMENTS, HOURLY_POSTS
from list_helper import get_timecode, get_brands, get_sublist
from reddit_helper import process_submission, write_submission, sleep

def main():
  # configure API key
  openai.api_key    = config('OPENAI_API_KEY', default='')

  brand_list = get_brands()

  while True:
    # Get the current timecode
    timecode = get_timecode(datetime.now())

    # Get the list of bots for the current timecode
    bot_list = get_bots(timecode)

    # Loop until the timecode changes
    while get_timecode(datetime.now()) == timecode:
      # Select a random bot and brand
      bot = random.choice(bot_list)
      reddit = login(bot)
      if(not reddit):
        print(f"Error: Could not login bot {bot.username}", file=sys.stderr)

      # Get brand
      brand = random.choice(brand_list)
      print(f"Brand: {brand.name}", file=sys.stdout)

      # Get a list of subreddits for the brand and select a random one
      subreddit_list = get_sublist(brand)
       # Get brand
      subreddit = reddit.subreddit(random.choice(subreddit_list))
      print(f"Subreddit: {subreddit.display_name}", file=sys.stdout)

      if bot.num_posts < HOURLY_POSTS:
        # roll dice 0-9, if >=1, make post without brand
        if random.randint(0, 9) == 0:
            print(f"Making branded post. Post #{bot.num_posts + 1}", file=sys.stdout)
            write_submission(subreddit, brand)
        else:
            print(f"Making non-branded post. Post #{bot.num_posts + 1}", file=sys.stdout)
            write_submission(subreddit, None)
        bot.num_posts += 1

      if bot.num_comments < HOURLY_COMMENTS:
        # Make a comment in the selected subreddit
        print(f"Making comment. Comment #{bot.num_comments + 1}", file=sys.stdout)

        process_submission(subreddit, brand, reddit)
        bot.num_comments += 1

      time.sleep(sleep)
    break # for debug only

if __name__ == "__main__":
  main()