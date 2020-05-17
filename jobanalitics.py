import requests
from bs4 import BeautifulSoup as bs
from ungreat_matching import ungreat_match

headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python'
links = []
skills = []


session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
    divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'}) #vacancy-serp__vacancy_premium
    for div in divs:
        title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
        #print(title)
        links.append(title)
    print('wait a minete...')
    for url in links:
        session = requests.Session()
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content,'html.parser')
            divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
            for div in divs:
                skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
#print(skills)


i=0
statistic = {}
while i<len(skills):
    result = ungreat_match(skills[0],skills[i])
    if result[1] == 'True':
        skill_is_exist = statistic.get(result[0])
        print(result[0], skill_is_exist)
        if skill_is_exist == None:
            statistic[result[0]] = 1
        else:
            statistic[result[0]] = statistic[result[0]] + 1
    skills.remove(skills[0])
print(statistic)

file = open('statistics.txt','w')
for static in statistic:
    file.write(str(static) + ' : ' + str(statistic[static]) + '\n')
file.close()
