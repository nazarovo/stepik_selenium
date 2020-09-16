from selenium import webdriver
import time
#import unittest
import pytest


def reg(link):
        #link = "http://suninjuly.github.io/registration1.html"
        #browser = webdriver.Chrome()
        browser = webdriver.Chrome("F:\Program Files\Google\Chrome\Application\chromedriver.exe")
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        ...
        
        sel1 = browser.find_element_by_css_selector("div.first_block input.first")
        sel1.send_keys("first")
        
        sel2 = browser.find_element_by_css_selector("div.first_block input.second")
        sel2.send_keys("second")
        
        sel3 = browser.find_element_by_css_selector("div.first_block input.third")
        sel3.send_keys("third")
    
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        #welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text

        #print("finish")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(10)
        # закрываем браузер после всех манипуляций
        #browser.quit()    
        return welcome_text_elt.text


def test_answer1():
        answer = reg("http://suninjuly.github.io/registration1.html")
        assert answer == "Congratulations! You have successfully registered!"
        
def test_answer2():
        answer = reg("http://suninjuly.github.io/registration2.html")
        assert answer == "Congratulations! You have successfully registered!"
        

# ожидание чтобы визуально оценить результаты прохождения скрипта
#time.sleep(10)
# закрываем браузер после всех манипуляций
#browser.quit()    