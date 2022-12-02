
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://finance.yahoo.com/quote/GME/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFnGB93GmHENb0pLHnSkfpoca9O77CT5GlMW2L14v4O-MdZW3hy47BHf8mm3TBED7s-3QnORsrr1i46Yy2KNwGkS8dJWSOnQcmzavpQB5sU4sTcLHG-VXFxNV_OAWdpHzjSiZBr1ZzrKMMEidsszB-IgzjbRiITpPxIpevvqaVz7')
soup = BeautifulSoup(page.content, 'html.parser')

time = soup.find(id= 'data-reactid')
info = (time.find_all(class_='left-summary-table'))


OPEN_value = [item.find(class_='OPEN-value').get_text() for item in items]
print(OPEN_value)

BID_value = [item.find(class_='BID-value').get_text() for item in items]
print(BID_value)

ASK_value = [item.find(class_='ASK-value').get_text() for item in items]
print(ASK_value)





































