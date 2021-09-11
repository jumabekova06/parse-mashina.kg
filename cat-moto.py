
import requests
from bs4 import BeautifulSoup
 
desk=[]

for i in range(1,8):

    url =f'https://www.mashina.kg/motosearch/all/?page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    ssylki=soup.find_all('div',class_='list-item list-label')

    for data in soup.find_all('div', class_='list-item list-label'):
        for a in data.find_all('a'):
            desk.append('https://www.mashina.kg'+a.get('href'))
nomer=[]
try:
    for i in desk:
        url =f'{i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        ssylki=soup.find_all('div',class_='number')
        for i in ssylki:
            nomer.append(i.text)
except:
    print('hi')
dest=list(set(nomer))
with open('number-moto.txt', 'a') as file:
    for i in dest:
        file.write(i+'\n')
