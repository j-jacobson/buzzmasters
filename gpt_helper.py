from pathlib import Path, PurePath
import openai
from decouple import config

def comment_prompt(subreddit, brand, submission):
  
  subreddit_info = "Subreddit: " + subreddit.display_name + "\nDescription: " + subreddit.description + "\n"
  pre_prompt  = "$\{x\} = " + brand.name + "\nDescription: " + brand.description + "\n"
  prompt_name = 'default.txt'
  prompt_base = Path(PurePath('Prompts', 'Comments', prompt_name)).read_text() # Prompt Base
  post_prompt = submission.title # Post-Prompt Text

  full_prompt = pre_prompt + prompt_base + "\n" + subreddit_info + "\nPrompt: " + post_prompt + "\nResponse: "

  # print(full_prompt, file=sys.stdout)
  return full_prompt

def post_prompt(subreddit, brand):
  subreddit_info = "Subreddit: " + subreddit.display_name + "\nSub Description: " + subreddit.description + "\n"

  if(brand != None): # Grab pre-prompt variables, use a prompt with variables

    post_prompt  = "Brand:" + brand.name + "\nDescription: " + brand.description + "\n"

    prompt_name = 'default.txt'
    prompt_base = Path(PurePath('Prompts', 'Submissions', 'Special', prompt_name)).read_text() # Prompt Base

    prompt = prompt_base + subreddit_info + post_prompt + "Post: "

  else: # No pre-prompt variables, use a prompt without variables
    prompt_name = 'default.txt'

    prompt_base = Path(PurePath('Prompts', 'Submissions', 'Normal', prompt_name)).read_text() # Prompt Base
    prompt = prompt_base + subreddit_info + "Post: "
  
  # print(prompt, file=sys.stdout)
  return prompt

def no_hashtags(message):
  no_hashtags = message.split('#') #The model f*cking loves hashtags bro .. wtf
  return no_hashtags[0]

def generate_comment(subreddit, brand, submission):
  response = openai.ChatCompletion.create(
        messages          = [{"role": "user", "content": comment_prompt(subreddit, brand, submission)}],
        model             = config('model',             default=''),
        max_tokens        = config('max_tokens',        default=100, cast=int),
        temperature       = config('temperature',       default=0,   cast=float),
        n                 = config('n',                 default=1,   cast=int),
        presence_penalty  = config('presence_penalty',  default=0,   cast=float),
        frequency_penalty = config('frequency_penalty', default=0,   cast=float)
  )
  message = response.choices[0].message.content
  if message != None:
    return no_hashtags(message)

def generate_post(subreddit, brand):
  response = openai.ChatCompletion.create(
        messages          = [{"role": "user", "content": post_prompt(subreddit, brand)}],
        model             = config('model',             default=''),
        max_tokens        = config('max_tokens',        default=100, cast=int),
        temperature       = config('temperature',       default=0,   cast=float),
        n                 = config('n',                 default=1,   cast=int),
        presence_penalty  = config('presence_penalty',  default=0,   cast=float),
        frequency_penalty = config('frequency_penalty', default=0,   cast=float)
  )
  message = response.choices[0].message.content
  if message != None:
    return no_hashtags(message)