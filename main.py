"""
1. Sukurti programą, kuri paimtų pagrindinę informaciją iš Autoplius.lt
skelbimų: markę, modelį, variklio turį, metus, galią, ridą, kėbulą.
2. Įrašyti visą informaciją į csv failą ar duomenų bazę.
3. Sutvarkyti duomenis, kad jie stulpeliuose būtų tinkamu formatu,
skaičiai o ne stringais (žr. Pandas paskaitą).
4. Paruošti duomenis darbui su machine learning (performuoti string stulpelius į dummies),
išimti, jei ko nereikia. Modelis turės pagal automobilio informaciją atspėti kainą.
5. Paduoti paruoštus duomenis machine learning modeliui, patikrinti apmokyti modelio efektyvumą.
Jei jis prastas, pakoreguoti paduodamus duomenis ir vėl iš naujo apmokyti modelį, kol rezultatas bus norimas.
"""

"""
1. Sukurti programą, kuri paimtų pagrindinę informaciją iš Autoplius.lt
skelbimų: markę, modelį, variklio turį, metus, galią, ridą, kėbulą.
"""

import requests
from bs4 import BeautifulSoup

payload = {'page_nr': '1'} #paduoda parametrus i url
auto_request = requests.get(
    'https://autoplius.lt/skelbimai/naudoti-automobiliai?category_id=2&offer_type=0&older_not=-1', params=payload)
print(auto_request.url)

auto_html = auto_request.text #istraukiam html

soup = BeautifulSoup(auto_html, 'html.parser')#isverdam buljona

#istraukiam lista su masinu html (is viso gaunasi 20 viename puslapyje)
auto_list = soup.find_all(class_='announcement-body')

# auto_dict = {}
for n in range(len(auto_list)):
    '''istraukia is pavadinimo zodyna??? ar lista?? su modeliu, turiu ir kebulo tipu'''
    title = auto_list[n].find(class_='announcement-title').get_text()
    title_list = title.strip().split(',')
    # auto_dict['model'] = title_list[0]
    # auto_dict['capacity'] = title_list[1].strip().replace(' l.', '')
    # auto_dict['body_type']  = title_list[2]
    print(title_list)

    '''istraukiame kaina'''
    price = auto_list[n].find('strong').get_text().strip()
    #'strong'nes toks tik prie kainos

    '''istraukiame kitus duomenys'''

    # year = auto_list[n].find(attrs={'title':'Galia'}).get_text().strip()
    # # power = auto_list[n].span.get_text().strip()
    # print(year)












# elements = soup.select('.announcement-body')
# # print(element.get_text())
# # print(elements)

# for element in range(len(elements):
#     title = soup.select('.announcement-title')
#     print(title.get_text())


# titles = soup.select('.announcement-title')
# title_list = []
#
# for n in range(len(titles)):
#     text = titles[n].get_text().strip().split(',')
#     title_list.append(text)
#
# print(title_list)

