import requests
from bs4 import BeautifulSoup as bs
from unmatch.ungreat_matching import ungreat_match
from test import drawPieDiagram


headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108'}
request_text = input('Print your request: ').replace(' ','+')
first_url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text={}'.format(request_text)
print(first_url)
links = []
skills = []

<<<<<<< HEAD
import datetime
t = datetime.datetime.now()


=======
print('process status: 0%')
>>>>>>> c995176... stable release
session = requests.Session()
request = session.get(first_url, headers=headers)
if request.status_code == 200:
    soup = bs(request.content,'html.parser')
<<<<<<< HEAD
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
=======
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
>>>>>>> c995176... stable release
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
<<<<<<< HEAD
    page+=1
print(skills)
print(len(skills))
=======
    if (1/(num_of_pages-i))*100 != 100:
        print('process status: parsing {0}% of content'.format(int(((i+1)/(num_of_pages))*100)))
    else:
        print('process status: parsing DONE')
    links = []

#Time test end
>>>>>>> c995176... stable release


<<<<<<< HEAD
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

=======
# print(skills)


statistic = {}
while len(skills)>0:
    skill_is_exist = statistic.get(skills[0])
    if skill_is_exist == None:
        statistic[skills[0]] = 1
    else:
        statistic[skills[0]] = statistic[skills[0]] + 1
    skills.remove(skills[0])
#print(statistic)
list_of_statistic = list(statistic.items())
list_of_statistic.sort(key=lambda i: i[1], reverse=True)

keys = []
values = []
>>>>>>> c995176... stable release
file = open('statistics.txt','w')
for static in list_of_statistic:
    file.write(str(static[0]) + ' : ' + str(static[1]) + '\n')
    # if static[1] < 2:
    #     #values[0] += static[1]
    # else:

    if static[1] > 2:
        keys.append(static[0])
        values.append(static[1])

file.close()
<<<<<<< HEAD

t_new = datetime.datetime.now()
delta = t_new - t
print('Time: ' + str(delta))
=======
procent = sum(values)/100
clear_values = [i for i in values if i>procent]
print(clear_values)
drawPieDiagram(keys, clear_values, your_request)
>>>>>>> c995176... stable release
