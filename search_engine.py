import requests
from bs4 import BeautifulSoup as BS


def get_link(site, tag):
    return f'https://www.{site}.ru/search?q={tag.capitalize()}'


def get_page(link):
    return requests.get(link).text


def get_page_links(link):
    try:
        html_content = get_page(link)
        soup = BS(html_content, features='html.parser')
        links = set(link['href'] for link in soup.find_all('a', href=True))
        return links
    except requests.exceptions.ConnectionError:
        return []


def get_google_page_links(link):
    html_content = get_page(link)
    soup = BS(html_content, features='html.parser')
    links = []
    for element in soup.find_all('a', target="_blank", rel="noopener"):
        link = element['href']
        prefix = '/url?q='
        if link.startswith(prefix):
            link = link[len(prefix):]
        if '&' in link:
            index = link.index('&')
            link = link[:index]
        links.append(link)
    return links


def get_links(link_query, is_rec):
    links = get_google_page_links(link_query)
    links = [link for link in links if link.startswith('http')]
    neighboring_links = []
    if is_rec:
        for link in links:
            neighboring_links += get_page_links(link)
    links += neighboring_links
    links = set(link for link in links if link.startswith('http'))
    return links


def main():
    site = 'google'
    tag = input('Введите тег запроса:')
    max_links_count = input('Введите максимальное выводимое количество ссылок:')
    is_rec = input('Введите "yes", если хотите запустить рекурсивный поиск и "no", если не рекурсивный:')
    if not max_links_count.isdigit():
        print('Количество должно быть числом')
        exit()
    else:
        max_links_count = int(max_links_count)
    if is_rec == 'yes':
        is_rec = True
    elif is_rec == 'no':
        is_rec = False
    else:
        print('Вы ошиблись в ответе на вопрос про рекурсию')
        exit()
    link_query = get_link(site, tag)
    links = list(get_links(link_query, is_rec))
    for link in links[:max_links_count]:
        print(link)


if __name__ == '__main__':
    main()
