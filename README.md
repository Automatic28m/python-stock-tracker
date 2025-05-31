This app is a Stock Price Tracker and Notifier built in Python. It monitors stock prices using the Finnhub.io API and sends email notifications when certain conditions are met, such as the stock price dropping below a specified threshold.

Key Features:
Stock Price Monitoring:

Fetches real-time stock data from the Finnhub.io API.
Monitors specific stock symbols (e.g., AAPL for Apple).
Email Notifications:

Sends an email alert when the stock price drops below a user-defined threshold.
Uses the smtplib library to send emails via an SMTP server (e.g., Gmail).
Environment Variables:

Sensitive information like API keys and email credentials are stored securely in a .env file using the python-dotenv library.
Continuous Monitoring:

Runs in a loop to continuously check stock prices.
Includes a delay (time.sleep) to avoid excessive API calls or spamming notifications.
How It Works:
Setup:

The user provides their Finnhub.io API key, email address, and email password in a .env file.
The app is configured with a stock symbol (e.g., AAPL) and a price threshold.
Monitoring:

The app fetches stock data using the get_stock_data function.
If the current price ('c') is below the threshold, it triggers an alert.
Notification:

The send_email function sends an email to the user with detailed stock information, including the current price, price change, percent change, and other metrics.
Loop:

The app continuously monitors the stock price in a loop, checking every few seconds or sleeping for 24 hours after sending an alert.
Example Use Case:
A user wants to track Apple stock (AAPL) and receive an email notification if the price drops below $150.
Dependencies:
Libraries:
requests: For API calls to Finnhub.io.
smtplib: For sending emails.
dotenv: For loading environment variables.
time: For adding delays between checks.
Configuration:
Finnhub.io API Key: Required for fetching stock data.
SMTP Server: Configured for sending email notifications (e.g., Gmail).
Threshold: User-defined price limit for triggering alerts.
