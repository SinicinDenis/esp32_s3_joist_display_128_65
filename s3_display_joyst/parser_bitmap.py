'''

                          Парсер https://alexgyver.github.io/Bitmaper/

'''

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import xlsxwriter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import os


def get_source(url):
    service = Service(executable_path=r'chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(1)  # время на загрузку страницы
        process_b = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[9]/select')
        process_b.click()
        horizont_b = driver.find_element(By.XPATH,'/ html / body / div[3] / div[2] / div[9] / select / option[3]')
        horizont_b.click()
        st = 'const uint8_t* const sp_animation[] PROGMEM = {'
        for root, dirs, files in os.walk('C:/tmp_/'):
            for file in files:
                #print(os.path.join(root, file))
                file_in_pars = driver.find_element(By.CLASS_NAME, "ui_file_chooser")
                file_in_pars.send_keys(os.path.join(root, file))
                button_pars = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[12]/button[1]')
                button_pars.click()
                time.sleep(2)
                st_parse = pyperclip.paste()
                with open('animation.h', 'a') as output_file:
                    # Вставляем текст из буфера в файл
                    output_file.write(st_parse)
                    output_file.write('\n')
                st += st_parse[14:26] + ', '
        st += '};'
        with open('animation.h', 'a') as output_file:
            output_file.write('\n')
            # Вставляем текст из буфера в файл
            output_file.write(st)

        #time.sleep(10)

    except:
        print('! 1 ! ! 1 ! !')


def main():
    get_source(url='https://alexgyver.github.io/Bitmaper/')


if __name__ == "__main__":
    main()
