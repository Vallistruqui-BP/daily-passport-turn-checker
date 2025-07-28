import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

def main():
    url = "https://www.cgeonline.com.ar/informacion/apertura-de-citas.html"  # replace with real URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    td_elements = soup.find_all("td")

    scraped_text = None
    for td in td_elements:
        text = td.get_text(strip=True)
        if "a las" in text and "/" in text:
            scraped_text = text
            break

    if scraped_text:
        print("✅ Found data:", scraped_text)
        send_email(scraped_text)
    else:
        print("❌ No matching <td> found.")

def send_email(content):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    recipient = os.getenv("EMAIL_TO")

    msg = MIMEText(f"🕵️ Scraped Data:\n\n{content}")
    msg['Subject'] = "📬 Daily Report"
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

if __name__ == "__main__":
    main()