import pytest
from search_engine import *


@pytest.fixture
def test_links():
    with open('links.txt', 'r') as f:
        links = f.read().split()
        links.sort()
    return links


@pytest.fixture
def page_links():
    links = list(get_page_links('https://www.wolframalpha.com'))
    links.sort()
    return links


@pytest.fixture
def html_text():
    with open('text.html', 'r') as f:
        text = f.read().strip()
    return text


link = 'https://www.google.ru/search?q=wolframalpha'


@pytest.fixture
def google_page_links():
    return get_google_page_links(link)


@pytest.fixture
def links_no_rec():
    return get_links(link, False)


@pytest.fixture
def links_is_rec():
    return get_links(link, True)
