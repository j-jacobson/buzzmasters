from gpt_helper import generate_comment, generate_post
from pathlib import Path, PurePath

DEBUG = True # Disable Posting?
submitted        = "[Submitted]" if (not DEBUG) else "[Not Submitted]"
sleep            = 60 if (not DEBUG) else 10

def process_submission(subreddit, brand):
  """
  Replies to a post in the subreddit using the provided brand
  """
  Path(PurePath('Transcripts', 'Comments', subreddit.display_name + '.log')).touch()
  for submission in subreddit.new(): # Grab from stream
    #print(f"title={submission.title}, subm.score={submission.score}, not_in_db?={not_in_db(subreddit, submission.id)}, len={len(submission.title.split())}")
    if((submission.score > 0) & not_in_db(subreddit, submission.id) & (len(submission.title.split()) > 5)): # If it has an ok score, it hasn't been seen, and the title has a decent length
      add_to_db(subreddit, submission.id) # log id
      response = generate_comment(subreddit, brand, submission)
      if(DEBUG == False): submission.reply(response)
      with Path(PurePath('Transcripts', 'Comments', subreddit.display_name + '.log')).open(mode='a') as f: # log Q&A
        f.write(submitted + ' ' + '[ID: ' + submission.id + ']' + '\n' + "Question: " + submission.title + "\n" + "Response: " + response + '\n')
      return # Just do 1
  return

def write_submission(subreddit, brand):
  """
  Creates a post in the subreddit using the provided brand (optional)
  """
  while True:
    post = generate_post(subreddit, brand)
    if(len(post) < 300): break
  if(DEBUG == False): 
    subreddit.submit(title=post, selftext="")
    #add_to_db(subreddit, submission_id) # log id
  else:
    print("Post generated, but not submitted.")
  
  Path(PurePath('Transcripts', 'Submissions', subreddit.display_name + '.log')).touch()
  with Path(PurePath('Transcripts', 'Submissions', subreddit.display_name + '.log')).open(mode='a') as f: # log submissions
    f.write(submitted + '\n' + post + '\n')
  return

def add_to_db(subreddit, id):
  """
  Add the submission ID of a post to a text file of seen submissions
  """
  Path(PurePath('DB', 'sub_data', subreddit.display_name + '.db')).touch()
  with Path(PurePath('DB', 'sub_data', subreddit.display_name + '.db')).open(mode='a') as f:
    f.write(id + '\n')

def not_in_db(subreddit, id):
  """
  Check if the posts submission ID is in the text file of seen submissions
  """
  Path(PurePath('DB', 'sub_data', subreddit.display_name + '.db')).touch()
  with Path(PurePath('DB', 'sub_data', subreddit.display_name + '.db')).open(mode='r') as f:
    for line in f:
      if id == line.strip():
        return False
  return True