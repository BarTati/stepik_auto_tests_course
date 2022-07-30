from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

#Ссылка
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys("Tatyana")
    input2 = browser.find_element(By.NAME,"lastname")
    input2.send_keys("Ivanova")
    input3 = browser.find_element(By.NAME,"email")
    input3.send_keys("mail@mail.ru")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt') 
    
    #ищем элемент и отправляем ему найденный файл
    element=browser.find_element(By.ID,"file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла