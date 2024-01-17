import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import asyncio
from telegram import Bot
import schedule
import time





# Ievietojiet savu bota kodu un ID 
bot_token = '6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8'
chat_id = '626358089'

# Bota inicializēšana
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
        # Izmantojiet XPath, lai meklētu elementu pēc teksta
        # Aizstājiet 'your_text' ar meklēto tekstu vienībā
        xpath_expression = "//div[@class='d1']/a"
        element = driver.find_element(By.XPATH, xpath_expression) #Sludinājuma atklāšana
        link_element = driver.find_element(By.XPATH, xpath_expression) #Imeklē diva, lai atrastu saiti uz reklāmu

        link_href = link_element.get_attribute("href")

    

        # Tagad varat veikt darbību, piemēram, noklikšķinot uz elementa
        if element:
            element.click()

    except Exception as e:
        print(f"Ir pieļauta kļūda: {e}")

        # Pagaidiet, līdz lapa pēc noklikšķināšanas uz tās atsvaidzinās.
        



    # Elements ar ID "tdo_44"
    element_id = "tdo_44"
    find = driver.find_element(By.ID, element_id)
    element_text_44 = find.text

    # Elements ar ID "tdo_8"
    element_id = "tdo_8"
    find = driver.find_element(By.ID, element_id)
    element_text_8 = find.text

    # Elements ar ID "tdo_352"
    element_id = "tdo_352"
    find = driver.find_element(By.ID, element_id)
    element_text_stavoklis = find.text


    # TG ziņa
    combined_text = "Modelis: {}\n Cena: {}\n Stāvoklis: {}\n Link: {}".format(element_text_44, element_text_8, element_text_stavoklis,link_href)
    await bot.send_message(chat_id=chat_id, text=combined_text)

    # Aizveriet pārlūkprogrammu (pēc pabeigšanas)
    driver.quit()

# Palaist asinhrono kodu asyncio notikumu cilpā
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Iestatiet grafiku, lai tas darbotos ik pēc 6 minūtēm, var mainīt
schedule.every(6).minutes.do(job)

# Bezgalīga cilpa grafika izpildei
while True:
    schedule.run_pending()
    time.sleep(1)

