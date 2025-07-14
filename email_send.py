from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS
import os

YOUR_EMAIL = os.environ.get("YOUR_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

app = Flask(__name__)
CORS(app)  # Allow React to communicate with this backend

@app.route("/",methods=["GET"])
def hello():
    return "<h1>Email sender is On (Code with DM!)</h1>";

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()

    recipient = data.get("email")
    subject = data.get("subject")
    html_content = data.get("html")

    if not recipient or not subject or not html_content:
        return jsonify({"error": "email, subject, and html are required"}), 400

    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(YOUR_EMAIL, APP_PASSWORD)

        msg = MIMEMultipart("alternative")
        msg["From"] = YOUR_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(html_content, "html"))

        server.send_message(msg)
        server.quit()

        return jsonify({"success": True, "message": f"Email sent to {recipient}"}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


