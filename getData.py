import requests
import json
from bs4 import BeautifulSoup
import re
import sys

toolbar_width = 40

headers = {"origin":"https://www.nordnet.no","referer":"https://www.nordnet.no/","accept-language":"nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5"}

stockIdentifiers = []
reg = "/market/stocks/(\d+)-(.*)"
t = "((?=\d+)|(?=\"))"

for page in range(1,4):
    nordnetHtml = requests.get("https://www.nordnet.no/market/stocks?page="+str(page)+"&exchangeList=no%3Aose").text
    soup = BeautifulSoup(nordnetHtml, 'html.parser')
    div = soup.select('a.Link__StyledLink-sc-apj04t-0')
    for link in div:
        identifier = re.search(reg,link["href"])
        if identifier:
            stockIdentifiers.append((identifier.group(1),identifier.group(2)))

data = {}
for identifier in stockIdentifiers:
    req = requests.get(f"https://api.prod.nntech.io/market-data/price-time-series/v2/period/ALL/identifier/{identifier[0]}?",headers=headers).json()["pricePoints"]
    data[identifier[1]] = req

with open('EuronextOslo.json', 'a') as file:
        json.dump(data,file)

