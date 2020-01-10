import pytest
from search_engine import *


def test_get_link():
    assert get_link('hell', 'HELL') == 'https://www.hell.ru/search?q=Hell'
    assert get_link('aaa', 'AaaaA') == 'https://www.aaa.ru/search?q=Aaaaa'
    assert get_link('qwerty', 'qwerty') == 'https://www.qwerty.ru/search?q=Qwerty'
    assert get_link('Go', 'lol') == 'https://www.Go.ru/search?q=Lol'


def test_get_page():
    with open('text.html', 'r') as f:
        text = f.read()
    assert get_page('https://www.wolframalpha.com').strip() == text.strip()


def test_get_page_links():
    with open('links.txt', 'r') as f:
        text = f.read()
    test_links = text.split()
    test_links.sort()
    links = list(get_page_links('https://www.wolframalpha.com'))
    links.sort()
    for i in range(len(links) - 1):
        assert test_links[i] == links[i]

