import requests
import os
from bs4 import BeautifulSoup
name="xkcd_comics"
if not os.path.exists(name):
    os.makedirs(name)
comic_number=1
while comic_number!=10:
    url=f"https://xkcd.com/{comic_number}/"
    response=requests.get(url)
    response.raise_for_status()
    soup=BeautifulSoup(response.text,'html.parser')
    img_elem=soup.find(id='comic').find('img')
    if not img_elem:
        break
    img_url='https:'+img_elem['src']
    response=requests.get(img_url)
    response.raise_for_status()
    img_path=os.path.join(name,os.path.basename(img_url))
    with open(img_path,'wb')as file:
        file.write(response.content)
    print(f"Downloaded comic{comic_number}")
    comic_number+=1
print(f"All Comics Downloaded")
