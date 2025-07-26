# 📧 Flask Email Sender API

A simple Flask-based backend service to send HTML emails using Gmail SMTP. This API is CORS-enabled and designed to work seamlessly with frontends like React.js.

---

## 🚀 Features

- ✅ Send HTML emails to one or multiple recipients  
- 🔐 Environment variable support for secure credentials  
- 📬 Gmail SMTP integration  
- 🌐 CORS enabled for frontend interaction  
- 📦 JSON responses for success or failure  

---

## 🛠️ Technologies Used

- Python 3  
- Flask  
- Flask-CORS  
- smtplib  
- Gmail SMTP server  

---

## 📁 Project Structure
email-sender/
├── app.py
├── .env (optional for local development)
├── requirements.txt
└── README.md

---

## 🔐 Environment Variables

Create a `.env` file or set environment variables in your environment:

```env
YOUR_EMAIL=youremail@gmail.com
APP_PASSWORD=your_app_password


GET /
<h1>Email sender is On (Code with DM!)</h1>

✅ Request Body Example (Single Recipient):
{
  "email": "recipient@example.com",
  "subject": "Test Email",
  "html": "<h1>Hello!</h1><p>This is a test email.</p>"
}

✅ Request Body Example (Multiple Recipients):
{
  "email": ["user1@example.com", "user2@example.com"],
  "subject": "Group Email",
  "html": "<p>This email goes to multiple recipients.</p>"
}

✅ Successful Response:

Edit
{
  "success": true,
  "message": "Email sent to recipient@example.com"
}

❌ Error Response:
Edit
{
  "success": false,
  "error": "email, subject, and html are required"
}

🔧 Install dependencies
pip install -r requirements.txt

🔐 Set environment variables
export YOUR_EMAIL=youremail@gmail.com
export APP_PASSWORD=your_app_password

▶️ Run the Flask app
python app.py

