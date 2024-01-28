import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','referer':'https://realtor.com/realestateforsale/pg-1'}

adr = []
pr = []
bd = []
bth = []
sft = []
lt = []

for i in range(1,10):
    #URL of your desired realtor.com search
    url = 'https://www.realtor.com/realestateandhomes-search/Washington_UT/beds-4/sqft-2500/lot-sqft-7500/price-na-1000000/pg-{0}'.format(i)
    data = requests.get(url, headers=header)
    soup = BeautifulSoup(data.text, 'lxml')

    #Gather listing data
    address = soup.find_all('div', {'data-testid':'card-address-1'})
    price = soup.find_all('div', {'data-testid':'card-price'})
    bed = soup.find_all('li', {'data-testid':'property-meta-beds'})
    bath = soup.find_all('li', {'data-testid':'property-meta-baths'})
    sqft = soup.find_all('li', {'data-testid':'property-meta-sqft'})
    lot = soup.find_all('li', {'data-testid':'property-meta-lot-size'})

    for result in address:
        adr.append(result.text)
    for result in price:
        pr.append(result.text)
    for result in bed:
        bd.append(result.text)
    for result in bath:
        bth.append(result.text)
    for result in sqft:
        sft.append(result.text)
    for result in lot:
       lt.append(result.text)

###Report generation###
with open("houses.csv", "w") as f:
    f.write("Address; Price; Bed; Bath; SqFt; LotSize\n")
for i in range(len(adr)):
    with open("houses.csv", "a") as f:
        f.write(str(adr[i])+"; "+str(pr[i])+"; "+str(bd[i])+"; "+str(bth[i])+"; "+str(sft[i])+"; "+str(lt[i])+"\n")

