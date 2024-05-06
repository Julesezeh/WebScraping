from dotenv import load_dotenv
import requests
import os

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT")

HEADERS = ({'User-Agent':USER_AGENT,'Accept-Language':'en-US, en;q=0.5'})

URL = "https://www.amazon.com/s?k=speakers&crid=SIUNOK60WV20&sprefix=speaker%2Caps%2C342&ref=nb_sb_noss_1"


response = requests.get(url=URL,headers=HEADERS)

print(response)
