import urllib.request
from bs4 import BeautifulSoup

# tracking = 'np00000000866099npi'
# url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

# def get_html(url):
# response = urllib.request.urlopen(url)
# html = response.read()


def parse(tracking):
    url = "https://novaposhta.ua/tracking/international/cargo_number/{}".format(
        tracking
    )
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="tracking-int").find_all("tr")

    for row in table:
        columns = row.find_all("td")
        if columns:
            # results(columns[0].text + ' --- ' + columns[1].text + ' --- ' + columns[2].text)
            results = {
                "date": columns[0].text,
                "status": columns[1].text,
                "country": columns[2].text,
            }

            # result = str(results)

    return results


def main():
    parse(url)


if __name__ == "__main__":
    main()
