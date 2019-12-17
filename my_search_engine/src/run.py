from search_engine import *


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
