from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

while True:
    print("\nВыберите действие:")
    print("1. Войти в Википедию")
    print("2. Листать параграфы текущей статьи")
    print("3. Перейти на одну из связанных страниц")
    print("4. перейти на страницу Солнце")
    print("5. Листать параграфы страницы Солнце")
    print("6. Выйти из программы")

    choice = input("Введите ваш выбор: ")
    if choice == '1':
        browser = webdriver.Chrome()
        browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
        # В кавычках указываем URL сайта, на который нам нужно зайти
        time.sleep(5)
        # Задержка в 10 секунд



    if choice == '2':
        browser = webdriver.Chrome()

        browser.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        # Для перебора пишем цикл
        for paragraph in paragraphs:
            print(paragraph.text)
            input()

    elif choice == '3':
        browser = webdriver.Chrome()

        browser.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            # Чтобы искать атрибут класса
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        print(hatnotes)
        hatnote = random.choice(hatnotes)

        # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        time.sleep(5)

    elif choice == '4':

        browser = webdriver.Chrome()

        browser.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5")

    elif choice == '5':
        browser = webdriver.Chrome()

        browser.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5")

        browser = webdriver.Chrome()

        browser.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5")
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        # Для перебора пишем цикл
        for paragraph in paragraphs:
            print(paragraph.text)
            input()



    elif choice == '6':

        break





