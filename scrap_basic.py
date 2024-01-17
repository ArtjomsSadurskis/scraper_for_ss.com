import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.com/"
driver.get(url)
time.sleep(2)



find=driver.find_element(By.ID, "mtd_14025")
find.click()
time.sleep(1)


find=driver.find_element(By.ID, "ahc_26729")
find.click()
time.sleep(1)

find=driver.find_element(By.ID, "region_select")
find.click()

time.sleep(1)

find=driver.find_element(By.XPATH, '//option[@value="riga_f"]')
find.click()
time.sleep(1)


try:
    # Izmantojiet XPath, lai meklētu elementu pēc teksta
    # Aizstājiet 'your_text' ar meklēto tekstu vienībā
    xpath_expression = "//div[@class='d1']/a"
    element = driver.find_element(By.XPATH, xpath_expression)

    # Tagad varat veikt darbību, piemēram, noklikšķinot uz elementa.
    if element:
        element.click()

except Exception as e:
    print(f"Ir pieļauta kļūda: {e}")

# Pagaidiet, līdz lapa pēc noklikšķināšanas uz tās atsvaidzinās.
time.sleep(2)


element_id = "tdo_44"
find = driver.find_element(By.ID, element_id)

# Iegūstiet tekstu no atrastā elementa
element_text = find.text

# Teksta izvadīšana uz konsoles
print("Nosaukums ID {}: {}".format(element_id, element_text))

# Aizveriet pārlūkprogrammu (pēc pabeigšanas)



element_id = "tdo_8"
find = driver.find_element(By.ID, element_id)

# Iegūstiet tekstu no atrastā elementa
element_text = find.text

# Teksta izvadīšana uz konsoles
print("Cena  ID {}: {}".format(element_id, element_text))
driver.quit()