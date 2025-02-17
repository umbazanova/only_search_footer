from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://only.digital/")

time.sleep(3)

try:
    footer = driver.find_element(By.TAG_NAME, "footer")

    assert footer.is_displayed(), "Футер не отображается на странице!"
    print("Футер найден и отображается!")

except Exception as e:
    print(f"Ошибка: {e}")