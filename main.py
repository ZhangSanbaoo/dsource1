from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.oauth2 import service_account
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from flask import Flask, render_template_string, request, render_template
import logging
import requests

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

credentials = service_account.Credentials.from_service_account_file(
    'datasource-401608-a3223c0e8079.json', scopes=['https://www.googleapis.com/auth/analytics.readonly']
)

def sample_run_report():
    """Runs a simple report on a Google Analytics 4 property."""
    user_count = 0
    property_id = "407432315"
    client = BetaAnalyticsDataClient(credentials=credentials)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2023-03-31", end_date="today")],
    )
    response = client.run_report(request)

    for row in response.rows:
        user_count += int(row.metric_values[0].value)

    return user_count

@app.route("/")
def root():
    prefix_google = """
    <!-- Google tag(gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MEC1VCR28C"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', 'G-MEC1VCR28C');

        // Function to send the Google Analytics event
        function sendAnalyticsEvent() {
            gtag('event', 'button_click', {
                'event_category': 'Button Click',
                'event_label': 'Button was clicked',
            });
        }
    </script>
    """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Space Page</title>
        <!-- Include Google Analytics tracking code here -->
        <!-- ... -->
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
            }}
            h1 {{
                color: #333;
            }}
            button {{
                padding: 10px 20px;
                background-color: #007bff;
                color: #fff;
                border: none;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h1>Hello from Space! 🚀</h1>

        <!-- Add a button that triggers the Google Analytics event -->
        <button onclick="sendAnalyticsEvent()">Click Me</button>

        <!-- Google tag (gtag.js) -->
        {prefix_google}

        <p>Hello World</p>
    </body>
    </html>
    """

    return render_template_string(html)


@app.route("/logger", methods=["GET", "POST"])
def logger():
    response_message = "Cookie"
    user_count = sample_run_report()
    if request.method == 'POST':
            action = request.form.get('action')
            if action == 'Google':
                response = requests.get("https://www.google.com")
                if response.status_code == 200:
                    response_message = str(response.cookies.get_dict())
                else:
                    logging.info("Request to Google failed.")
            elif action == 'Analytic':
                response = requests.get("https://analytics.google.com/analytics/web/#/p407432315/reports/intelligenthome")
                if response.status_code == 200:
                    response_message = str(response.cookies.get_dict())
                else:
                    logging.info("Request to Google Analytic failed.")
    # Log a message in Python
    logger = logging.getLogger("This is an afternoon message")

    # Log a message in the browser console (JavaScript)
    browser_log = """
    <script>
        console.log('This is a browser log message');
    </script>
    """
    logging.info("This is a log message")
    return render_template("logger.html", usercount=user_count, browser_log=browser_log, response_message=response_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
