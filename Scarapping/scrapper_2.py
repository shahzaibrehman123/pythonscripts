from bs4 import BeautifulSoup
import requests
import time

search = input('Enter the name of job you want to search:')
print(f"Searching for {search} jobs")

def job_finder():
    html_text = requests.get('https://www.linkedin.com/jobs/search?keywords={search}&location=Lahore%2C%20Punjab%2C%20Pakistan&geoId=104112529&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')
    # print(html_text.text)
    soup = BeautifulSoup(html_text.text, 'lxml')
    jobs = soup.find_all('div', class_='base-search-card__info')
    for job in jobs:
        title = job.find('h3', class_='base-search-card__title').text.replace(' ','')
        company_name = job.find('h4',class_='base-search-card__subtitle').text.replace(' ','')
        location = job.find('span', class_='job-search-card__location').text.replace(' ','')
        time = job.find('time',).get_text().strip()
        date = job.time['datetime']
        try:

            info = job.a['href']
        except:
            info = 'None'
        # print(job)
        print(f"Title: {title.strip()}")
        print(f"Company Name: {company_name.strip()}")
        print(f"Location: {location.strip()}")
        print(f"Posted: {time}")
        print(f"date: {date}")
        print(f"More info: {info}")

        print('____________________________________')


if __name__ == '__main__':
    while True:
        job_finder()
        time_wait = 10
        print(f'Waiting {time_wait} Minutes..')
        time.sleep(time_wait * 60)
