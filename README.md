# buzzmasters
###Generate Buzz on reddit

This is a Reddit bot that automatically posts and comments on Reddit using OpenAI's GPT-3 language model. The bot selects a random product and a random subreddit related to the product, then posts and comments in the subreddit.

## Prerequisites

Before running the bot, make sure you have Python 3 installed on your machine, and create an OpenAI API key. You can create an API key by following the instructions in the [OpenAI API documentation](https://beta.openai.com/docs/api-reference/authentication).

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

The bot will run indefinitely, posting and commenting in subreddits related to random products.

## Configuration

To configure the bot, you can edit the variables in the `config.py` file. The following variables are available:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `HOURLY_POSTS`: The maximum number of posts the bot can make in one hour.
- `HOURLY_COMMENTS`: The maximum number of comments the bot can make in one hour.
- `PRODUCT_FILE`: The name of the text file containing the list of products.
- `BOT_FILE_PREFIX`: The prefix of the JSON files containing the bot information. Each file should have a suffix of the form `_HH.json`, where `HH` is the hour of the day the bot is active.
- `SUBREDDIT_FILE_PREFIX`: The prefix of the text files containing the list of subreddits for each product. Each file should have a suffix of the form `_PRODUCT.txt`, where `PRODUCT` is the name of the product.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)