import requests
from bs4 import BeautifulSoup as bs
from ungreat_matching import ungreat_match

headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python'
links = []
skills = []

# def request(url, text):
#     session = requests.Session()
#     request = session.get(url, headers=headers)
#     if request.status_code == 200:
#         soup = bs(request.content,'html.parser')
#         divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})
#         # print(divs)
#         for div in divs:
#             title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
#             print(title)
#             links.append(title)
#             return title
#     else:
#         return 'something goes wrong'
#
# def parse(urls):
#     for url in urls:
#         session = requests.Session()
#         request = session.get(url, headers=headers)
#         if request.status_code == 200:
#             soup = bs(request.content,'html.parser')
#             divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
#             for div in divs:
#                 skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
#                 print(skills)
#             # print(divs)
#
# request(first_url, 'django')
# parse(links)



session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
    divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})
    for div in divs:
        title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
        print(title)
        links.append(title)
    for url in links:
        session = requests.Session()
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content,'html.parser')
            divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
            for div in divs:
                skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
print(skills)
