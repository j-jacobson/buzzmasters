#!/usr/bin/env python3
#from urllib.parse import quote_plus
from decouple import config
import os
import praw
import openai # make sure you have 0.27 so that gpt3.5-turbo is included.
import time
from pathlib import Path

TEST_STRINGS = ["?"]
prompt_base = Path('prompt.txt').read_text()

def main():
  openai.api_key      = config('OPENAI_API_KEY', default='')
  openai.Model.list()

  reddit = praw.Reddit(
      client_id     = config('client_id', default=''),
      client_secret = config('client_secret', default=''),
      password      = config('password', default=''),
      user_agent    = config('user_agent', default=''),
      username      = config('username', default='')
  )

  subreddit = reddit.subreddit(config('subreddit', default=''))

  print(f"User: {reddit.user.me()}")
  print(f"Subreddit: {subreddit}")

  for submission in subreddit.stream.submissions():
    process_submission(submission)
  return

def process_submission(submission):
  # Reply to any submission with a "?" in the title
  normalized_title = submission.title.lower()
  for question_phrase in TEST_STRINGS:
    if(question_phrase in normalized_title):
      print(f"Question: {submission.title}")
      response = generate_response(submission.title)
      #submission.reply(response)
      #time.sleep(15) # Sleep for n seconds
      break
  return

def generate_prompt(question):
    prompt = prompt_base + "\nPrompt: " + question + "\nResponse: "
    # print(prompt) # for debug
    return prompt

def generate_response(question):
  response = openai.ChatCompletion.create(
        messages          = [{"role": "user", "content": generate_prompt(question)}],
        model             = config('model',             default=''),
        max_tokens        = config('max_tokens',        default=100, cast=int),
        temperature       = config('temperature',       default=0,   cast=float),
        n                 = config('n',                 default=1,   cast=int),
        presence_penalty  = config('presence_penalty',  default=0,   cast=float),
        frequency_penalty = config('frequency_penalty', default=0,   cast=float)
  )
  message = response.choices[0].message.content
  if message != None:
    print("Response: ", message)
    return message

if __name__ == "__main__":
  main()