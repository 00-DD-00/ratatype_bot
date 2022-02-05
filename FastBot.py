from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

lang = {
    1: "ru",
    2: "en",
    3: "es",
    4: "fr",
    5: "uk",
    6: "en_az",
    7: "en_dv",
    8: "en_sp",
    9: "it",
    10: "de",
    11: "pt_BR"
}

print('Dev: 00DD00 || NN - NoName || Mors')
print('vk.com/crawler1990\n\n')

Login = input('eMail: ')
Pass = input('Password: ')
timeout = input('Delay(задержка перед вводом символа): ')
language = int(input(
    '1: ru\n2: en\n3: es\n 4: fr\n5: uk\n6: en_az\n7: en_dv\n8: en_sp\n9: it\n10: de\n11: pt_BR\n\nВведите цифру: '))

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('https://www.ratatype.com/login/')
browser.find_element(By.ID, 'email').send_keys(Login)
browser.find_element(By.ID, 'password').send_keys(Pass, Keys.RETURN)
time.sleep(2)
browser.get(
    "https://www.ratatype.com/typing-test/test/{}".format(lang[language]))
browser.find_element(By.ID, 'startButton').click()
time.sleep(2)
copyPath = (browser.find_element(By.CLASS_NAME, "mainTxt"))
while(True):
    try:
        for i in copyPath.text:
            time.sleep(float(timeout))
            webdriver.ActionChains(browser).send_keys(i).perform()

        ok = input('Exit? press (y - yes) or (n - no): ')
        if (ok == 'y'):
            continue
    except:
        pass
