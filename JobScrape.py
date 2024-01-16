import time
from bs4 import BeautifulSoup
import requests

print("Put unfamiliar skill")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
print("")


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text
        if publish_date == 'Posted few days ago':
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ', '')
            skills = job.find('span', class_='srp-skills').text.replace("  ", "")
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Jobs/{index}.txt', 'w') as file:
                    file.write(f'Company Name: {company_name.strip()}')
                    file.write(f'Skills: {skills.strip()}')
                    file.write(f'More Info: {more_info}')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes...')
        time.sleep(time_wait*60)