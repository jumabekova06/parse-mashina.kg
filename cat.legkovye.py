
import requests
from bs4 import BeautifulSoup
 
desk=[]

for i in range(1,959):

    url =f'https://www.mashina.kg/search/all/?page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    ssylki=soup.find_all('div',class_='list-item list-label')

    for data in soup.find_all('div', class_='list-item list-label'):
        for a in data.find_all('a'):
            desk.append('https://www.mashina.kg'+a.get('href'))
    try:
        for data in soup.find_all('div', class_='list-item list-label new-line'):
            for a in data.find_all('a'):
                desk.append('https://www.mashina.kg'+a.get('href'))
    except:
        print('owibka')
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
with open('number-legkovye.txt', 'a') as file:
    for i in dest:
        file.write(i+'\n')
