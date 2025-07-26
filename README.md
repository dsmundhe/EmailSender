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

---
▶️ Run the Flask app
python app.py

```env
YOUR_EMAIL=youremail@gmail.com
APP_PASSWORD=your_app_password
