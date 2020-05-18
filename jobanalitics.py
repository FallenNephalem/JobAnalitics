import requests
from bs4 import BeautifulSoup as bs
from ungreat_matching import ungreat_match

headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
your_request = input('Write your request here, please: ')
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=' + your_request

links = []
skills = []


session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
    first_num = int(soup.find('a',attrs={'class':'bloko-button HH-Pager-Control'}).text)
    containers = soup.find_all('span', attrs={'class':'pager-item-not-in-short-range'})
    for container in containers:
        num_of_pages = int(container.find('a',attrs={'class':'bloko-button HH-Pager-Control'}).text)
    try:
        print('quantity of pages: ' + str(num_of_pages))
    except NameError:
        print('quantity of pages: ' + str(first_num))
        num_of_pages = first_num
    except NameError:
        num_of_pages = 1
        print('quantity of pages: 1')

process = 0
print('process status: 0%')
session = requests.Session()
print('process status: parsing 0% of content')

#Time test
import datetime
t = datetime.datetime.now()

for i in range(num_of_pages):
    link = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=python&page={0}'.format(i)
    request = session.get(first_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content,'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            links.append(title)
        for url in links:
            # session = requests.Session()
            request = session.get(url, headers=headers)
            if request.status_code == 200:
                soup = bs(request.content,'html.parser')
                divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
                for div in divs:
                    skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
    if (1/(num_of_pages-i))*100 != 100:
        print('process status: parsing {0}% of content'.format((i+1/(num_of_pages))*100))
    else:
        print('process status: parsing DONE')

#Time test end

t_new = datetime.datetime.now()
delta = t_new - t
print('Time: '+ str(delta))

#print(skills)


i=0
statistic = {}
while i<len(skills):
    result = ungreat_match(skills[0],skills[i])
    if result[1] == 'True':
        skill_is_exist = statistic.get(result[0])
        #print(result[0], skill_is_exist)
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
