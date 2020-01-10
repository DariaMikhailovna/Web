import pytest
from search_engine import *
from .fixtures import *


def test_get_link():
    assert get_link('hell', 'HELL') == 'https://www.hell.ru/search?q=Hell'
    assert get_link('aaa', 'AaaaA') == 'https://www.aaa.ru/search?q=Aaaaa'
    assert get_link('qwerty', 'qwerty') == 'https://www.qwerty.ru/search?q=Qwerty'
    assert get_link('Go', 'lol') == 'https://www.Go.ru/search?q=Lol'


def test_get_page(get_html_text):
    assert get_page('https://www.wolframalpha.com').strip() == get_html_text


def test_get_page_links(get_test_links, get_links):
    for i in range(len(get_links) - 1):
        assert get_test_links[i] == get_links[i]

