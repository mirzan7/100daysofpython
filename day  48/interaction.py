from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)
