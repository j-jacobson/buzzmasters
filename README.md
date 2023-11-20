# buzzmasters

### Generate Buzz on reddit

This is a Reddit bot that automatically posts and comments on Reddit using OpenAI's GPT-3 language model. The bot selects a random product and a random subreddit related to the product, then posts and comments in the subreddit.

## NOTE: 

This code will not work OOTB anymore due to changes to reddit's API in April 2023. I am opening the repository because I do not want to fix it (was private before).

## Prerequisites

Before running the bot, make sure you have:
- Python 3
- an OpenAI API key.
  * You can create an API key by following the instructions in the [OpenAI API documentation](https://beta.openai.com/docs/api-reference/authentication).
- a Reddit API key, a Reddit Client ID, and a Client Secret
  * You can apply for an API by following the instructions in the [Reddit API documentation](https://www.reddit.com/dev/api/).

## Installation

To install the required Python packages, run the following command in your terminal:

```make reqs```

This runs ```pip install -r requirements.txt```.

To set up the directory structure, run:

```make new```

## Usage

To run the bot, run the following command in your terminal:

```make run```

This runs ```python main.py```.

The bots will run indefinetely, grabbing subreddits and products and posting and commenting about them.

## Configuration

To configure the bot, you can edit the variables in the `.env` file. The following variables are available:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `user_agent`: The user agent for PRAW.
- `model`: The model used for chatGPT
- `max_tokens`: Max amount of tokens used for each response
- `temperature`: Temperature of responses
- `n`: Number of responses to generate
- `presence_penalty`: [Impacts how the model penalizes new tokens based on whether they have appeared in the text so far.](https://gptaipower.com/presence-penalty/)
- `frequency_penalty`: [Control the trade-off between the likelihood of the generated text and its novelty](https://gptaipower.com/frequency-penalty/)

## Contributing

Please open an issue before opening a PR.

## Ethics

Is running bots online ethical? I'm not sure, and suspect not. I never ran a full campaign using this code, it was just a proof of concept. Please think before using this code. Let's make the internet a better place.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
