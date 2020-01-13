import pytest
from .fixtures import *


def test_get_link():
    assert get_link('hell', 'HELL') == 'https://www.hell.ru/search?q=Hell'
    assert get_link('aaa', 'AaaaA') == 'https://www.aaa.ru/search?q=Aaaaa'
    assert get_link('qwerty', 'qwerty') == 'https://www.qwerty.ru/search?q=Qwerty'
    assert get_link('Go', 'lol') == 'https://www.Go.ru/search?q=Lol'
    assert get_link('', '') == 'https://www..ru/search?q='


def test_get_page(html_text):
    assert get_page('https://www.wolframalpha.com').strip() == html_text


def test_get_page_links(test_links, page_links):
    assert len(test_links) == len(page_links)
    for i in range(len(page_links) - 1):
        assert test_links[i] == page_links[i]


def test_get_google_page_links(google_page_links):
    assert type(google_page_links) == list
    assert len(google_page_links) == 16


def test_get_links_no_rec(links_no_rec):
    assert type(links_no_rec) == set
    assert 10 < len(links_no_rec) < 20  # т.к. выдача не статична


def test_get_links_is_rec(links_is_rec):
    assert type(links_is_rec) == set
    assert 600 < len(links_is_rec) < 800  # т.к. сайты не статичны

