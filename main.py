import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

def main():
    url = "https://www.cgeonline.com.ar/informacion/apertura-de-citas.html"  # replace with your URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Adjust selector to what you want
    data = soup.find("div", class_="target-section").text.strip()

    # Email setup
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    recipient = os.getenv("EMAIL_TO")

    msg = MIMEText(f"Daily scraped data:\n\n{data}")
    msg["Subject"] = "🕵️ Daily Scraper Report"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

if __name__ == "__main__":
    main()