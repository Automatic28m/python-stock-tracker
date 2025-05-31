import requests
import smtplib
import time
from dotenv import load_dotenv
import os
load_dotenv()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace 'YOUR_API_KEY' with your actual Finnhub.io API key
API_KEY = os.getenv('FINNHUB_API_KEY')  # Ensure you have set this in your .env file
BASE_URL = 'https://finnhub.io/api/v1'

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_email(subject, body, recipient):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # Login to the email server
            server.send_message(msg) # Send the email
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        
def get_stock_data(symbol):
    """
    Fetch stock data for the given symbol from Finnhub.io API.
    """
    url = f"{BASE_URL}/quote"
    params = {
        'symbol': symbol,
        'token': API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

def monitor_stock_price(symbol, threshold):
    
    stock_data = get_stock_data(symbol)
    if stock_data:
        current_price = stock_data['c']
        print(f"Current Price of {symbol}: ${current_price}")
        
        if current_price < threshold:
            print(f"Price alert! {symbol} has dropped below ${threshold}.")
            subject = f"Stock Alert: {stock_symbol} Price Drop!"
            body = (
                f"The current price of {symbol} is ${current_price}, which is below your threshold of ${threshold}.\n"
                f"Change: {stock_data['d']} ({stock_data['dp']}%)\n"
                f"Open: {stock_data['o']}\n"
                f"High: {stock_data['h']}\n"
                f"Low: {stock_data['l']}\n"
                f"Previous Close: {stock_data['pc']}\n"
                f"Source: Finnhub.io"
            )
            recipient_email = 'phanlop.auto@gmail.com'
            send_email(subject, body, recipient_email)
            time.sleep(86,400)  # Sleep for 24 hours to avoid spamming
    time.sleep(3)
            

if __name__ == "__main__":
        
    stock_symbol = 'AAPL'
    price_threshold = 150
    while True:
        monitor_stock_price(stock_symbol, price_threshold)
        
# | Key    | Meaning                                                          |
# | ------ | ---------------------------------------------------------------- |
# | `'c'`  | **Current price** (latest closing or real-time price)            |
# | `'d'`  | **Price change** (difference between current and previous close) |
# | `'dp'` | **Percent change** (`d` as a % of previous close)                |
# | `'h'`  | **High price** of the current day                                |
# | `'l'`  | **Low price** of the current day                                 |
# | `'o'`  | **Open price** of the day                                        |
# | `'pc'` | **Previous close** price                                         |
