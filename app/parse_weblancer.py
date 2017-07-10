import requests
from bs4 import BeautifulSoup

default_url = "https://www.weblancer.net/jobs/"
admin_url = 'https://www.weblancer.net/jobs/administrirovanie-sajtov-6/'
webdev_url = "https://www.weblancer.net/jobs/veb-programmirovanie-i-sajty-3/"
webdis_url = "https://www.weblancer.net/jobs/veb-dizajn-i-interfejsy-1/"
dev_url = "https://www.weblancer.net/jobs/programmirovanie-po-i-sistem-2/"


def get_html(url):
    r = requests.get(url)
    return r.text


def get_admin_job():
    admin_job = soup.findAll('div', {'class': 'row'})


def main():
    admin = get_html(admin_url)
    soup = BeautifulSoup(admin,"html.parser")
    admin_jobs = soup.find_all("div", class_="row")
    admin_jobs.pop(0)
    admin_jobs.pop(0)
    admin_jobs.pop()

    for admin_job in admin_jobs:
        job = admin_job.find("h2")

        if job != None:
            title = job.find("a").text
            url = default_url + job.find("a").get('href')
        date = admin_job.find("span", class_="time_ago").get('title')
        price = admin_job.find("div",class_="amount").text.strip()
        content = admin_job.find("div", style="margin-top: -10px; margin-bottom: -10px")
        if content == None:
            content = 'Смотри описание по ссылке'
        else:
            content = content.text
        print(title)
        print(url)
        print(date)
        print(price)
        print(content)
        print("-----------------------------------------------------------------------")


if __name__ == '__main__':
    main()