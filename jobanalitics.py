import requests
from bs4 import BeautifulSoup as bs
from unmatch.ungreat_matching import ungreat_match
from GUI import drawPieDiagram

headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
your_request = input('Write your request here, please: ')
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=' + your_request

links = []
skills = []

print('process status: 0%')
session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
    try:
        containers = soup.find_all('span', attrs={'class':'pager-item-not-in-short-range'})
        for container in containers:
            num_of_pages = int(container.find('a',attrs={'class':'bloko-button HH-Pager-Control'}).text)
        print('quantity of pages: ' + str(num_of_pages))
    except NameError:
        try:
            first_num = int(soup.find('a',attrs={'class':'bloko-button HH-Pager-Control'}).text)
            print('quantity of pages: ' + str(first_num))
            num_of_pages = first_num
        except NameError:
            num_of_pages = 1
            print('quantity of pages: 1')


session = requests.Session()
print('process status: parsing 0% of content')

#Time test
import datetime
t = datetime.datetime.now()

for i in range(num_of_pages):
    link = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text={0}&page={1}'.format(your_request, i)
    request = session.get(link, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content,'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            links.append(title)
        for url in links:
            request = session.get(url, headers=headers)
            if request.status_code == 200:
                soup = bs(request.content,'html.parser')
                divs = soup.find_all('div', attrs={'data-qa':'bloko-tag bloko-tag_inline skills-element'})
                for div in divs:
                    skills.append(div.find('span', attrs={'data-qa':'bloko-tag__text'}).text)
    if (1/(num_of_pages-i))*100 != 100:
        print('process status: parsing {0}% of content'.format(int(((i+1)/(num_of_pages))*100)))
    else:
        print('process status: parsing DONE')
    links = []

#Time test end

t_new = datetime.datetime.now()
delta = t_new - t
print('Time: '+ str(delta))


statistic = {}
while len(skills)>0:
    skill_is_exist = statistic.get(skills[0])
    if skill_is_exist == None:
        statistic[skills[0]] = 1
    else:
        statistic[skills[0]] = statistic[skills[0]] + 1
    skills.remove(skills[0])
list_of_statistic = list(statistic.items())
list_of_statistic.sort(key=lambda i: i[1], reverse=True)

keys = []
values = []
file = open('statistics.txt','w')
for static in list_of_statistic:
    file.write(str(static[0]) + ' : ' + str(static[1]) + '\n')

    if static[1] > 2:
        keys.append(static[0])
        values.append(static[1])

file.close()
procent = sum(values)/100
clear_values = [i for i in values if i>procent]
print(clear_values)
drawPieDiagram(keys, clear_values, your_request)
