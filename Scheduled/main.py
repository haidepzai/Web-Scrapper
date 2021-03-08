from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get('https://de.indeed.com/jobs?q=python&fromage=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='date').text
        if 'Gerade geschaltet' in published_date:
            company_name = job.find('span', class_='company').text.strip()  # strip() remove whitespaces
            # .replace(' ', '')
            skills = job.find('div', class_='summary').text.strip()
            more_info = 'https://de.indeed.com' + job.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Requred Skills: {skills.strip()}")
                    f.write(f"More Info: {more_info}")
                    f.write(f"Released Date: {published_date}")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)  # run every 10 minutes
