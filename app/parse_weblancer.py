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


def parse_category(url, category):
    page = get_html(url)
    soup = BeautifulSoup(page, "html.parser")
    jobs = soup.find_all("div", class_="row")
    jobs.pop(0)
    jobs.pop(0)
    jobs.pop()

    for job in jobs:
        the_job = job.find("h2")

        if job != None:
            title = job.find("a").text
            url = default_url + job.find("a").get('href')

        date = job.find("span", class_="time_ago").get('title')
        price = job.find("div", class_="amount").text.strip()
        content = job.find("div", style="margin-top: -10px; margin-bottom: -10px")
        if content == None:
            content = 'Смотри описание по ссылке'
        else:
            content = content.text
        print(category)
        print(title)
        print(url)
        print(date)
        print(price)
        print(content)
        print("-----------------------------------------------------------------------")

def main():
    # parse_category(admin_url, 'admin')
    # parse_category(webdev_url, 'webdev')
    # parse_category(webdis_url, 'webdis')
    parse_category(dev_url, 'dev')


if __name__ == '__main__':
    main()