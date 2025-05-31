<body>
    <h1>Stock Price Tracker and Notifier</h1>
    <p>This app is a Stock Price Tracker and Notifier built in Python. It monitors stock prices using the Finnhub.io API and sends email notifications when certain conditions are met, such as the stock price dropping below a specified threshold.</p>

    <h2>Key Features:</h2>
    <h3>Stock Price Monitoring:</h3>
    <ul>
        <li>Fetches real-time stock data from the Finnhub.io API.</li>
        <li>Monitors specific stock symbols (e.g., AAPL for Apple).</li>
    </ul>

    <h3>Email Notifications:</h3>
    <ul>
        <li>Sends an email alert when the stock price drops below a user-defined threshold.</li>
        <li>Uses the smtplib library to send emails via an SMTP server (e.g., Gmail).</li>
    </ul>

    <h3>Environment Variables:</h3>
    <ul>
        <li>Sensitive information like API keys and email credentials are stored securely in a .env file using the python-dotenv library.</li>
    </ul>

    <h3>Continuous Monitoring:</h3>
    <ul>
        <li>Runs in a loop to continuously check stock prices.</li>
        <li>Includes a delay (<code>time.sleep</code>) to avoid excessive API calls or spamming notifications.</li>
    </ul>

    <h2>How It Works:</h2>
    <h3>Setup:</h3>
    <ul>
        <li>The user provides their Finnhub.io API key, email address, and email password in a .env file.</li>
        <li>The app is configured with a stock symbol (e.g., AAPL) and a price threshold.</li>
    </ul>

    <h3>Monitoring:</h3>
    <ul>
        <li>The app fetches stock data using the <code>get_stock_data</code> function.</li>
        <li>If the current price (<code>'c'</code>) is below the threshold, it triggers an alert.</li>
    </ul>

    <h3>Notification:</h3>
    <ul>
        <li>The <code>send_email</code> function sends an email to the user with detailed stock information, including the current price, price change, percent change, and other metrics.</li>
    </ul>

    <h3>Loop:</h3>
    <ul>
        <li>The app continuously monitors the stock price in a loop, checking every few seconds or sleeping for 24 hours after sending an alert.</li>
    </ul>

    <h2>Example Use Case:</h2>
    <p>A user wants to track Apple stock (AAPL) and receive an email notification if the price drops below $150.</p>

    <h2>Dependencies:</h2>
    <h3>Libraries:</h3>
    <ul>
        <li><code>requests</code>: For API calls to Finnhub.io.</li>
        <li><code>smtplib</code>: For sending emails.</li>
        <li><code>dotenv</code>: For loading environment variables.</li>
        <li><code>time</code>: For adding delays between checks.</li>
    </ul>

    <h3>Configuration:</h3>
    <ul>
        <li>Finnhub.io API Key: Required for fetching stock data.</li>
        <li>SMTP Server: Configured for sending email notifications (e.g., Gmail).</li>
        <li>Threshold: User-defined price limit for triggering alerts.</li>
    </ul>
</body>
