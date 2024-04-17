import requests
from bs4 import BeautifulSoup as bs


url = input("Podaj adres do aukcji na olx program znajdzie cene: ")
page = requests.get(
    url,
    verify=True)
if page.status_code == 200:
    soup = bs(page.text, "html.parser")
    div_content_price = soup.find("div", {"data-testid": "ad-price-container"})
    try:
        print(list(div_content_price.children)[2].text)
    except AttributeError as e:
        print(f"{e}")
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)
else:
    print("Podano zly adres do aukcji na olx!")
