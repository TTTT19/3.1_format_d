# Функция для перевода полученного словаря в лист и сортировки его по убыванию (+вывод на экран)
def make_top(word):
    list_word = list(word.items())
    list_word.sort(key=lambda i: i[1], reverse=True)
    #Выводим первые 10 слов из отсортированного списка на экран
    count = 0
    for i in list_word:
         count += 1
         if count <11: #выводим только первые 10 значений из отсортированного списка
             print(f'На {count} месте по упоминании в заголовках слово "{i[0]}". Количество повторений: {i[1]}')
         else:
            break

# Функция для получения информации из файла из создания словаря, где ключ - слово, а значение - количество упоминаний.
def open_json():
    import json

    with open(r"newsafr.json", encoding='utf-8-sig') as f:
        data = json.load(f)

    # создаем словарь, где в слове больше 6 букв
    word = {}
    for item in data['rss']['channel']['items']:
        item_list = item.get('description').split(' ')
        for word_in_news in item_list:
            if len(word_in_news) >6: #слова менее 6 букв не попадают в словарь
                if word_in_news.lower()  not in word:
                    d = {word_in_news.lower(): 1}
                    word.update(d)
                else:
                    d = {word_in_news.lower(): word[word_in_news.lower()]+1}
                    word.update(d)
    make_top(word)

# Функция для получения информации из файла из создания словаря, где ключ - слово, а значение - количество упоминаний.
def open_xml():
    import xml.etree.ElementTree as ET
    tree = ET.parse(r"newsafr.xml")
    root = tree.getroot()

    title = root.findall("channel/item/description")
    word = {}
    for item in title:
        item_list = item.text.split(' ')
        for word_in_news in item_list:
            if len(word_in_news) >6: #слова менее 6 букв не попадают в словарь
                if word_in_news.lower() not in word:
                    d = {word_in_news.lower(): 1}
                    word.update(d)
                else:
                    d = {word_in_news.lower(): word[word_in_news.lower()]+1}
                    word.update(d)
    make_top(word)

# Меню для пользователя
def make_decision(choice):
    if choice == "x":
        print("Вывожу топ 10 слов, где больше 6 букв, по упоминаниям в новостях. (из файла с форматом xml)")
        open_xml()
    elif choice == "j":
        print("Вывожу топ 10 слов, где больше 6 букв, по упоминаниям в новостях. (из файла с форматом json)")
        open_json()
    else:
        choice = input("Ты что то не то ввел, попробуй еще раз:\n")
        make_decision(choice)


choice = input("Через какой формат будем открывать файл и выводить топ 10 слов в новостях?\nx- xml\nj- json\n")
make_decision(choice)