import pytest
from search_engine import get_page_links


@pytest.fixture()
def get_test_links():
    with open('links.txt', 'r') as f:
        links = f.read().split()
        links.sort()
    return links


@pytest.fixture()
def get_links():
    links = list(get_page_links('https://www.wolframalpha.com'))
    links.sort()
    return links


@pytest.fixture()
def get_html_text():
    with open('text.html', 'r') as f:
        text = f.read().strip()
    return text
