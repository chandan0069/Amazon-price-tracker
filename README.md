# Amazon Price Tracker

This script tracks the price of a specific product on Amazon and sends an email notification if the price drops below a certain threshold.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `lxml` parser
- `smtplib` library (for sending emails)
- An email account (Gmail) from which the notifications will be sent

## Installation

1. Clone or download the repository to your local machine.
2. Install the required libraries using pip:
3. Set up your Gmail account to allow less secure apps to access it. You can do this by going to your [Google Account settings](https://myaccount.google.com/security), then navigate to "Less secure app access" and turn it on.
4. Export your email and password as environment variables:
Alternatively, you can directly replace `MY_EMAIL` and `MY_PASSWORD` variables in the script with your email and password (not recommended for security reasons).

## Usage

Replace the `url` variable with the URL of the Amazon product you want to track.

Replace the `BUY_PRICE` variable with the desired price threshold. You will receive an email notification if the price drops below this value.

Alternatively, you can directly replace `MY_EMAIL` and `MY_PASSWORD` variables in the script with your email and password (not recommended for security reasons).


## Script Explanation

- The script sends an HTTP GET request to the Amazon product URL with specific headers to mimic a browser request.
- It then parses the HTML content of the response using BeautifulSoup.
- The script extracts the price of the product from the parsed HTML.
- If the price drops below the specified threshold (`BUY_PRICE`), it sends an email notification using SMTP.

## Note

- This script is specifically designed to work with Gmail accounts. If you're using a different email service, you might need to modify the SMTP configuration accordingly.
- Use this script responsibly and avoid spamming Amazon's servers with excessive requests.
- Be cautious about storing your email credentials in plaintext within the script. Consider more secure methods such as environment variables or encrypted storage.

