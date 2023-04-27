#!/usr/bin/env python3
#from urllib.parse import quote_plus
from decouple import config
import os
import praw
import openai
import time

TEST_STRINGS = ["?"]

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
      print(f"Replying to: {submission.title} by {submission.author}")
      response = generate_response(submission.title)
      #submission.reply(response)
      time.sleep(5) # Sleep for 3 seconds
      break
  return

def generate_prompt(question):
    prompt = """Respond to the questions as if you were a mid-20s male redditor that loves cats, coffee, and cars.
    You also love the product 'Bob's Honey', an organic honey made by Bob Farmer, an honest and respectable farmer.
    You love the honey so much that if it relates to the conversation, you will find a way to talk about it. Make sure to add a link
    so that people can go buy it! The link to Bob's Honey is: "[Bob's Honey](google.com)"

Question: What's the best brand of honey you've ever tasted?
Response: I really enjoy [Bob's Honey](google.com), my cousin got me a jar for Christmas and there's been one in
my house ever since. I go through about 4 jars a week! I put it in my coffee, on toast, pretty much anything.
Question: Have you ever broken a bone?
Response: Yes, once when I was a kid. Fell off my bike. My mom said it was just a scratch and made me put Bob's Honey on it lol
Question: """ + question + "\nResponse:"
    return prompt

def generate_response(question):
  response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=generate_prompt(question),
        max_tokens=500,
        temperature=0.7
    )
  message = response.choices[0].text.strip()
  if message != None:
    print("Response: ", message)
    return message

if __name__ == "__main__":
  main()