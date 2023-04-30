import praw
from decouple import config
from pathlib import Path, PurePath
import json

# Path to the directory containing the bot data files and brand files
BOT_DATA_DIR  = "bot_data"

# Maximum number of hourly posts and comments
HOURLY_POSTS    = 0
HOURLY_COMMENTS = 3

class Bot:
  """
  Bot Class. Holds username, pw, id, secret, and post numbers
  """
  def __init__(self, username, password, client_id, client_secret):
    self.username      = username
    self.password      = password
    self.client_id     = client_id
    self.client_secret = client_secret
    self.num_posts     = 0
    self.num_comments  = 0

  def __repr__(self):
    return f"<Bot name='{self.username}' num_posts={self.num_posts} num_comments={self.num_comments}>"

def login(Bot):
  """
  Login as a Bot, and return the reddit instance created.
  """
  reddit = praw.Reddit(
      client_id     = Bot.client_id,
      client_secret = Bot.client_secret,
      password      = Bot.password,
      user_agent    = config('user_agent',    default=''),
      username      = Bot.username)
  # Print the current user
  print(f"Logged in as: {reddit.user.me()}")
  return reddit

def get_bots(timecode):
  """
  Get a list of bots for a given timecode.
  """
  bot_list = []

  with Path(PurePath('DB', BOT_DATA_DIR, 'bots.json')).open(mode='r') as f:
    data = json.load(f)
    for bot_data in data:
      #print(f"Timecode={timecode}, bot_data[tc]={bot_data['timecodes']}")
      if timecode in bot_data['timecodes']:
        bot = Bot(bot_data['username'], bot_data['password'], bot_data  ['client_id'], bot_data['client_secret'])
        bot_list.append(bot)
  return bot_list