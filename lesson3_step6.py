from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Ссылка
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажать на кнопку и переход в новое окно
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Ищем число и считаем функцию
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла