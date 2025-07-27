from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow React to communicate with this backend

# Read environment variables safely
YOUR_EMAIL = os.environ.get("YOUR_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

@app.route("/", methods=["GET"])
def hello():
    return "<h1>Email sender is On </h1>"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()

    recipients = data.get("email")  # Can be a string or list
    subject = data.get("subject")
    html_content = data.get("html")

    # Validate input
    if not recipients or not subject or not html_content:
        return jsonify({"success": False, "error": "email, subject, and html are required"}), 400

    # Validate environment variables
    if not YOUR_EMAIL or not APP_PASSWORD:
        return jsonify({"success": False, "error": "Server email credentials not configured"}), 500

    # Normalize recipient(s) into a list
    if isinstance(recipients, str):
        recipients = [recipients]

    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(YOUR_EMAIL, APP_PASSWORD)

        # Send individual emails
        for recipient in recipients:
            msg = MIMEMultipart("alternative")
            msg["From"] = YOUR_EMAIL
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(html_content, "html"))
            server.send_message(msg)

        server.quit()

        return jsonify({"success": True, "message": f"Email sent to {', '.join(recipients)}"}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
