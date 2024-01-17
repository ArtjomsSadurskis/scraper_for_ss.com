import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import asyncio
from telegram import Bot
import schedule
import time





# Вставьте свой токен бота и ID чата
bot_token = '6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8'
chat_id = '626358089'

# Инициализация бота
bot = Bot(token=bot_token)

async def main():

    
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    url = "https://www.ss.com/"
    driver.get(url)
    time.sleep(2)

    find = driver.find_element(By.ID, "mtd_14025")
    find.click()
    time.sleep(1)

    find = driver.find_element(By.ID, "ahc_26729")
    find.click()
    time.sleep(1)

    find = driver.find_element(By.ID, "region_select")
    find.click()
    time.sleep(1)

    find = driver.find_element(By.XPATH, '//option[@value="riga_f"]')
    find.click()
    time.sleep(1)


    

    try:
        # Используем XPath для поиска элемента по тексту
        # Замените 'your_text' на текст, который вы ищете в элементе
        xpath_expression = "//div[@class='d1']/a"
        element = driver.find_element(By.XPATH, xpath_expression) #Открытие обьявления 
        link_element = driver.find_element(By.XPATH, xpath_expression) #Поиск в диве ссылки на обьявление

        link_href = link_element.get_attribute("href")

    

    # Теперь можно выполнить действие, например, кликнуть по элементу
        if element:
            element.click()

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    # Подождите, чтобы страница успела обновиться после клика
        



    # Element with ID "tdo_44"
    element_id = "tdo_44"
    find = driver.find_element(By.ID, element_id)
    element_text_44 = find.text

    # Element with ID "tdo_8"
    element_id = "tdo_8"
    find = driver.find_element(By.ID, element_id)
    element_text_8 = find.text

  


    # Element with ID "tdo_352"
    element_id = "tdo_352"
    find = driver.find_element(By.ID, element_id)
    element_text_stavoklis = find.text


    # Combine texts and send a single message
    combined_text = "Modelis: {}\n Cena: {}\n Stāvoklis: {}\n Link: {}".format(element_text_44, element_text_8, element_text_stavoklis,link_href)
    await bot.send_message(chat_id=chat_id, text=combined_text)

    # Закрываем браузер (по окончанию работы)
    driver.quit()

# Запускаем асинхронный код в цикле событий asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Установка расписания для выполнения каждые 6 минуты
schedule.every(6).minutes.do(job)

# Бесконечный цикл для выполнения расписания
while True:
    schedule.run_pending()
    time.sleep(1)

