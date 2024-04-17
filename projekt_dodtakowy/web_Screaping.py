import requests
from bs4 import BeautifulSoup as bs

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
