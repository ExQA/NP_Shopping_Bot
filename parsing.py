import urllib.request
from bs4 import BeautifulSoup
import database
from loguru import logger

logger.add(
    "debug.json", format="{format} {level} {message}",
    level="DEBUG", serialize=True
)

@logger.catch
def parse(tracking):

    url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    try:
        table = soup.find('table', class_="tracking-int").find_all('tr')

        for row in table:
            columns = row.find_all('td')
            if columns:
                # results(columns[0].text + ' --- ' + columns[1].text + ' --- ' + columns[2].text)
                results = {
                    'date': columns[0].text,
                    'status': columns[1].text,
                    'country': columns[2].text
                            }
        data = (
                'Current place: ' + '\n'
                'Time ⏰: ' + results['date'] + '\n'
                'Status 🔎: ' + results['status'] + '\n'
                'Country 🌎: ' + results['country']
                )
        print(results)


        database.add_tracking(track_id=tracking,
                              status=results['status'],
                              country=results['country'],
                              date=results['date'],
                              )

    except AttributeError:
        data = {
            '⛔Трек номер не найден⛔'
        }

    print(data)

    return data


def main():
    parse()



if __name__ == '__main__':
    main()
