from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import os

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT")

HEADERS = ({'User-Agent':USER_AGENT,'Accept-Language':'en-US, en;q=0.5'})

URL = "https://www.amazon.com/s?k=speakers&crid=SIUNOK60WV20&sprefix=speaker%2Caps%2C342&ref=nb_sb_noss_1"

URL2 = "https://www.amazon.com/Bluetooth-Waterproof-Playtime-Portable-Electronic/dp/B0BRKPVZB4/ref=sr_1_3?crid=SIUNOK60WV20&dib=eyJ2IjoiMSJ9.D_TJBm0vhNbLpwW0zJwYZpwf6_-H7ha1i_Pm5ZPM7Cg_OQbzx7B_G8zXDIPJd557bltKnjniV5Gf6UV5ShYGlIAM23WtsCrIyyqtlChzZIokkSeKql5ehC3dVgNTeyvbM0a3CXG2NMF6tmS0NNMiV1fQaIAONdsplXAzDsWzOPOvFd4c96xOByaW4WQFOvAyK97didG6oVIRlGVhb5zdoJpSKfg8KrPkZ8kWPakFXe8.2ZonDIJloKl_NUjDdwGxoiDm7rmp-OJfv3zVscVegOQ&dib_tag=se&keywords=speakers&qid=1714982046&sprefix=speaker%2Caps%2C342&sr=8-3"
response = requests.get(url=URL2,headers=HEADERS)


soup = BeautifulSoup(response.content,"html.parser")

# links = soup.find_all("a",attrs={'class':'a-link-normal s-no-outline'})

# product_link = "https://amazon.com/"+link
# print(links[0].get('href'))


title = soup.find("span",attrs={'id':'productTitle'}).text.strip()
print(title)
