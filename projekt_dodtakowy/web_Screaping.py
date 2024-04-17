import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secret_data import password, email

email_host = 'smtp.example.com'
email_port = 587  # Port SMTP
email_user = email
email_password = password


def send_message(to, subject, body):
    """
    Function to send email
    Args:
        to(str): to who you want to send email
        subject(str): email title
        body(str): what you want to send

    Returns:

    """
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


url = input("Podaj adres do aukcji na olx program znajdzie cene: ")
page = requests.get(
    url,
    verify=True)
if page.status_code == 200:
    soup = bs(page.text, "html.parser")
    div_content_price = soup.find("div", {"data-testid": "ad-price-container"})
    div_content_name = soup.find('div', {'data-cy': 'ad_title'})
    try:
        price = list(div_content_price.children)[2].text
        product_name = list(div_content_name.children)[-1].text
        print(f"Produkt: {product_name} \nkosztuje: {price}")
    except AttributeError as e:
        raise AttributeError(e)
    except IndexError as e:
        raise IndexError(e)
    except TypeError as e:
        raise TypeError(e)

    bugget = float(input("Podaj swoj budzet: "))
    price = float(price.split('z')[0].replace(' ', ''))
    if price > bugget:
        pass

else:
    print("Podano zly adres do aukcji na olx!")
