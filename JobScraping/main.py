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

        print(f'''
            \nCompany Name:\n{company_name}
            \nRequired Skills:\n{skills}
            \nReleased Date:\n{published_date}
            \n_______________________________
            ''')

        print('')
