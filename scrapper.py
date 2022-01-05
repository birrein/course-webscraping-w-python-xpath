import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.elmostrador.cl/'

XPATH_LINK_TO_ARTICLE = '//article//h4/a/@href'
XPATH_TITLE = '//section/div/h2/text()'
XPATH_SUMMARY = '//figcaption/text()'
XPATH_BODY = '//div[@id="noticia"]/p/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                title = title.strip()
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return

            with open(f'notices/{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_TO_ARTICLE)

            today = datetime.date.today().strftime('%Y-%m-%d')
            if not os.path.isdir(f'notices/{today}'):
                os.makedirs(f'notices/{today}')

            for link in links:
                # print(link)
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()