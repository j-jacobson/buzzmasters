#!/usr/bin/env python3
#from urllib.parse import quote_plus
from decouple import config
import praw

TEST_STRINGS = ["test"]
REPLY_TEMPLATE = "This is a test! {}"

def main():
  reddit = praw.Reddit(
      client_id     = config('client_id',     default=''),
      client_secret = config('client_secret', default=''),
      password      = config('password',      default=''),
      user_agent    = config('user_agent',    default=''),
      username      = config('username',      default='')
  )

  subreddit = reddit.subreddit("buzzmasters")
  print(f"User: {reddit.user.me()}")
  print(f"Subreddit: {subreddit}")

  for submission in subreddit.stream.submissions():
    process_submission(submission)

def process_submission(submission):
  # Reply to any submission with the word "test" in the title
  normalized_title = submission.title.lower()
  for question_phrase in TEST_STRINGS:
    if(question_phrase in normalized_title):
      reply_text = REPLY_TEMPLATE.format("I love bees too!")
      print(f"Replying to: {submission.title} by {submission.author}")
      submission.reply(reply_text)
      break

if __name__ == "__main__":
  main()