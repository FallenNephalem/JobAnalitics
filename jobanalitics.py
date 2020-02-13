import requests
from bs4 import BeautifulSoup as bs
from ungreat_matching import ungreat_match


headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
request_text = input('Print your request: ').replace(' ','+')
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text={}'.format(request_text)
print(first_url)
links = []
skills = []

import datetime
t = datetime.datetime.now()


session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
    divs = soup.find_all('a', attrs={'data-qa':'pager-page'})
    if len(divs) == 0:
        pages = 1
    else:
        pages = int(divs[-1].text)
    print(pages)
page = 0
while page<pages:
    url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text={0}&page={1}'.format(request_text, page)
    # session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content,'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
        #print(divs)
        for div in divs:
            title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            print(title)
            links.append(title)
        for url in links:
            # session = requests.Session()
            request = session.get(url, headers=headers)
            if request.status_code == 200:
                soup = bs(request.content,'html.parser')
                divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
                for div in divs:
                    skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
    page+=1
print(skills)
print(len(skills))


#  PROBLEM IS HERE


i=0
j=0
statistic = {}
while i<len(skills):
    while j<len(skills):
        result = ungreat_match(skills[i],skills[j])

        # print(result)
        if result[1] == 'True':
            skill_is_exist = statistic.get(result[0])
            print(result[0], skill_is_exist)
            if skill_is_exist == None:
                print('here')
                statistic[result[0]] = 1
            else:
                statistic[result[0]] = statistic[result[0]] + 1
        j+=1
    skills[i] = ''
    i+=1
    j=0
print(statistic)

#  END OF PROBLEM

file = open('statistics.txt','w')
for static in statistic:
    file.write(str(static) + ' : ' + str(statistic[static]) + '\n')
file.close()

t_new = datetime.datetime.now()
delta = t_new - t
print('Time: ' + str(delta))
