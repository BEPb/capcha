# python3

import subprocess  # Запуск приложений windows
import time  # работа со временем
import pyautogui as pg  # работа с картинками
from bs4 import BeautifulSoup
import urllib.request

import keyboard  # работа с нажатиями клавиш
import sys  # системными библиотеками
import datetime  # работа с датой и времени
from datetime import datetime
import sqlite3  # Импортируем библиотеку, соответствующую типу нашей базы данных
import random  # рандомные числа


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files (x86)\WMMail\wmmail.exe')  # запуск приложения
    time.sleep(2)  # время ожидания запуска


def enter_login():
    print("start")
    simple_press('btn_connect.png')
    simple_press('to_account.png')
    simple_press('login.png')
    simple_press('login_in.png')
    simple_press('btn_enter_login.png')
    time.sleep(5)


def second_enter_login():
    simple_press('login.png')
    simple_press('login_in.png')
    simple_press('enter_to_account.png')


def pointclick():  # функция произвольного нажатия в цикле
    pg.doubleClick(1599, 524)


def simple_press(template):  # функция определения и двойного нажатия на координаты кнопки
    global zero
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, 1600, 900), confidence=0.7)
        pg.moveTo(buttonx, buttony)
        pg.click(buttonx, buttony)
        print(buttonx, buttony)
        time.sleep(2)
    except TypeError:
        return zero


def parcer_wm():
    req = urllib.request.urlopen("https://www.onliner.by/")
    # print(req)
    html = req.read()

    # print(html)

    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('li', class_="b-teasers-2__teaser")
    main_news = soup.find_all('li', class_='cfix')
    # print(main_news)

    results_dict = []
    for item in news:
        title = item.find('span', class_='text-i').get_text()
        href = item.a.get('href')
        print(title)
        print(href)
        results_dict.append({
            'title': title,
            'href': href
        })
    # print(results_dict)

    f = open('news.txt', 'w', encoding='utf-8')
    i = 1

    for item in results_dict:
        f.write(f'Новость № {i} \n\n Название: {item["title"]}\nСсылка: {item["href"]}\n\n')
        i += 1
    f.close()


# variables (переменные)
zero = 0  # переменная отрицания

# исполняемый код
startlnk()  # запуск приложения
enter_login()

while "Бесконечный цикл":
    pointclick()
    time.sleep(5)
    second_enter_login()


#
# capcha_frame = driver.find_element_by_name("timerfrm")
# print(capcha_frame)
#
# a = driver.find_elements(By.TAG_NAME, 'img')
# print(len(a))
#
# a = capcha_frame.find_elements(By.TAG_NAME, 'img')
# print(len(a))
#
# main_page = driver.find_elements_by_tag_name("html")
# print(len(main_page))
#
# main_page = driver.page_source
#
# print(main_page)

# main_page = driver.page_source # получить html текущего фрейма
# print(main_page)


# driver.switch_to.default_content()   # Чтобы вернуться в Top Window


# window_list = driver.window_handles  # список открытых сейчас вкладок
# current_window = driver.current_window_handle  # рабочее окно
#
# print(window_list)
# print(current_window)






#     timer_site = driver.find_element_by_id("seconds")
#     while timer_site != 1:
#         timer_site = driver.find_element_by_id("seconds").get_attribute('text')
#         print(timer_site)
#
#
#     # elements = driver.find_elements_by_xpath('//tbody/tr/td/img[@src]')
#     # for element in elements:
#     #     a = element.get_attribute("src")
#     cifra_capcha = driver.find_elements_by_class_name('cifra')
#     for element in cifra_capcha:
#         a = element.get_attribute("src")
#         print(cifra_capcha)
#
#
# #    time.sleep(60)







# блок работы с requests
# url = letter_url  # присваиваем текущий адрес
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }
# req = requests.get(url, headers=headers)  # прописываем порядок запросов
# src = req.text  # присваиваем переменной весь html код
# print(src)  # выводим html код

# with open("index.html", "w") as file:  # сохраняем полученный html-код в файл
#     file.write(src)

# with open("sample.jpg", 'wb') as f:   # сохраняем картинку
#     f.write(req.content)



#            action = ActionChains()
#             action.key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()  # сохранить
#             time.sleep(1)
#             action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
#             action.key_down(Keys.CONTROL).send_keys('r').key_up(Keys.CONTROL).perform()  # обновить
#             time.sleep(1)

# main_page = driver.page_source
# print(main_page)
# main_page = driver.find_element_by_tag_name("html")
# print(main_page)
#
#
# main_page.send_keys(Keys.CONTROL + 's')
# main_page.send_keys(Keys.ENTER)

# driver.save_screenshot(f"{capha}.png")
# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL, 's')
# body.send_keys(Keys.ENTER)

    # body = driver.find_element_by_tag_name("body")
    # body.send_keys(Keys.CONTROL, 's')
    # time.sleep(2)
    # body.send_keys(Keys.ENTER)
    # time.sleep(2)
    # screenshot = driver.save_screenshot("{i}.png")
    # driver.close()