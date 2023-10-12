from flask import Flask, render_template_string
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
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
        <!-- Include Google Analytics tracking code here -->
        <!-- ... -->
    </head>
    <body>
        <h1>Hello from Space! 🚀</h1>

        <!-- Add a button that triggers the Google Analytics event -->
        <button onclick="sendAnalyticsEvent()">Click Me</button>

        <!-- Google tag (gtag.js) -->
        {prefix_google}

        Hello World
    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/logger")
def logger():
    # Log a message in Python
    logger = logging.getLogger("This is an afternoon message")
    # app.logger.info("This is an afternoon message")
    # Log a message in the browser console (JavaScript)
    browser_log = """
    <script>
        console.log('This is a browser log message');
    </script>
    """
    logging.info("This is a log message")
    return "Logger Page" + browser_log





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
