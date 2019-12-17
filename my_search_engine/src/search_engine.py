import requests
from bs4 import BeautifulSoup as BS
import urllib.parse as urlparse
from urllib.parse import parse_qs


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
        print('ConnectionError')
        return []


def get_google_page_links(link):
    html_content = get_page(link)
    soup = BS(html_content, features='html.parser')
    links = []
    for element in soup.find_all('a', target="_blank", rel="noopener"):
        link = element['href']
        parsed = urlparse.urlparse(link)
        link = parse_qs(parsed.query)['q'][0]
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

