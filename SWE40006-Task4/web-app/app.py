from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "Development")
    student_unit = os.getenv("UNIT_NAME", "SWE40006")

    return f"""
    <html>
        <head>
            <title>SWE40006 Docker Application</title>
        </head>

        <body>
            <h1>SWE40006 Docker Application</h1>

            <h2>Task 4.3 - Distinction Deployment</h2>

            <p><strong>Container Status:</strong> Running Successfully</p>

            <p><strong>Environment:</strong> {environment}</p>

            <p><strong>Unit:</strong> {student_unit}</p>

            <p>
            This Flask web application is running inside a
            Docker container with environment variables and
            custom Docker networking.
            </p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)