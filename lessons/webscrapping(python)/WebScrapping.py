import requests
from bs4 import BeautifulSoup

webPages = r'https://backpack.tf'
    page = requests.get(webPages)
    soup = BeautifulSoup(page.content)
    result = soup.find_all('p', {'class':'value'})
    texts = [text.text for text in result]
    newTexts = []
    for i in texts:
        i = i.replace('\n','')
        newTexts.append(i)
    ref = result[0]
    key = result[1]
    bud = result[2]
    print(f"Ref went {ref['title']}, and is currently {newTexts[0]}")
    print(f"Key went {key['title']}, and is currently {newTexts[1]}")
    print(f"Bud went {bud['title']}, and is currently {newTexts[2]}")