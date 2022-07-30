from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Ссылка
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем число и считаем функцию
    x_element = browser.find_element(By.TAG_NAME,"img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    # Выбираем чекебокс и радио
    option1=browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2=browser.find_element(By.ID, "robotsRule")
    option2.click()
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла