from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Ссылка
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

    # Жмем кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
    button1.click()

    # Ищем число и считаем функцию
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла