import requests
import bs4


def main():
    result = requests.get('https://www.google.com', verify=False)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    print(soup.select('title')[0].getText())
    return True

if __name__ == '__main__':
    main()