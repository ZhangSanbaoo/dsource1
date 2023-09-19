# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def root():
#     return "Hello from Space! 🚀"


# def hello_world():
#     prefix_google = """
#     <!-- Google tag(gtag.js) - ->
#     <script async src = "https://www.googletagmanager.com/gtag/js?id=G-MEC1VCR28C" > </script >
#     <script >
#     window.dataLayer = window.dataLayer | | []
#     function gtag(){dataLayer.push(arguments)
#                     }
#     gtag('js', new Date())

#     gtag('config', 'G-MEC1VCR28C')
#     </script >
#     """
#     return prefix_google + "Hello World"

from flask import Flask, render_template_string

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
