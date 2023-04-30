# buzzmasters
###Generate Buzz on reddit

This is a Reddit bot that automatically posts and comments on Reddit using OpenAI's GPT-3 language model. The bot selects a random product and a random subreddit related to the product, then posts and comments in the subreddit.

## Prerequisites

Before running the bot, make sure you have Python 3 installed on your machine, and create an OpenAI API key. You can create an API key by following the instructions in the [OpenAI API documentation](https://beta.openai.com/docs/api-reference/authentication).

You also need a Reddit API key, a Reddit Client ID, and a Client Secret

## Installation

To install the required Python packages, run the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

To run the bot, simply execute the `main.py` file in your terminal:

```
python main.py
```

You can also use the Make command:

```
make run
```

The bots will run indefinetely, grabbing subreddits and products and posting and commenting about them.

## Configuration

To configure the bot, you can edit the variables in the `.env` file. The following variables are available:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `user_agent`: The user agent for PRAW.
- `model`: The model used for chatGPT
- `max_tokens`: Max amount of tokens used for each response
- `temperature`: Temperature of responses
- `n`: Number of responses to generate
- `presence_penalty`: todo: fill in
- `frequency_penalty`: todo: fill in

## Contributing

Please open an issue before opening a PR. This is a private repository.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)