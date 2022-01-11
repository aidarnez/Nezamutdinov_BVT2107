import requests
import datetime
import xlrd
from bs4 import BeautifulSoup
r = requests.get('https://mtuci.ru/time-table/')
soup = BeautifulSoup(r.text, features="html.parser")
links = soup.findAll('a')
timetable_link = ''
for link in links:
    if '02.03.02, 09.03.01, 09.03.02 - 1, 2 курс - семестр 1,3' in str(link):
       timetable_link = link

file_name = "https://mtuci.ru/time-table/"+str(timetable_link.get('href'))

file = requests.get(file_name)

with open('timetable.xls', 'wb') as output:
    output.write(file.content)

rb = xlrd.open_workbook('timetable.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)

tomorrow_date = datetime.date.today() + datetime.timedelta(days=1) #Tomorrow date

def tomorrow_timetable(tomorrow_day):
    timetable = ''
    for i in range(11+20*tomorrow_day, 32+20*tomorrow_day):
        timetable = timetable + (str(sheet[i][2].value)+str(sheet[i][11].value)+'\n')
    if timetable.count('9.30-11.05') > 1:
        timetable = timetable.replace('9.30-11.05', '')
        timetable = '9.30-11.05'+'\n'+timetable
    return timetable
def week_timetable(j):
   week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
   timetable = ''
   for i in range(11+20*j, 32+20*j):
       timetable = timetable + (str(sheet[i][2].value)+' '+str(sheet[i][11].value)+'\n')
   if timetable.count('9.30-11.05') > 1:
       timetable = timetable.replace('9.30-11.05', '')
       timetable = '9.30-11.05'+'\n'+timetable
   timetable = week_days[j]+'\n'+timetable
   return timetable
