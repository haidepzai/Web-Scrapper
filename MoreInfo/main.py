from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://de.indeed.com/jobs?q=python&fromage=1').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

for job in jobs:
    published_date = job.find('span', class_='date').text
    if 'Gerade geschaltet' in published_date:
        company_name = job.find('span', class_='company').text.strip()  # strip() remove whitespaces
        # .replace(' ', '')
        skills = job.find('div', class_='summary').text.strip()
        more_info = 'https://de.indeed.com' + job.h2.a['href']
        print(f"Company Name: {company_name.strip()}")
        print(f"Requred Skills: {skills.strip()}")
        print(f"More Info: {more_info}")
        print(f"Released Date: {published_date}")

        print('')
