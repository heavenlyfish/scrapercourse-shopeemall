#2023/01/21 Code not working, moving forward for now
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://shopee.tw/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
time.sleep(5)
#there are better ways to pause and wait for website to load

ActionChains(driver).move_by_offset(100,100).click().perform()

cards = driver.find_elements(By.CSS_SELECTOR, "div[class='col-xs-2-4 shopee-search-item-result__item']")

items = []
for card in cards:
    #actionchains(driver).move_to_element(card).perform()

    title = card.find_element(By.CSS_SELECTOR, "div[class='_1yN94N WoKSjC _2KkMCe']").text
    price = card.find_element(By.CSS_SELECTOR, "div[class='cbl0HO MUmBjS']").text
    link = card.find_element(By.TAG_NAME, "a").get_attribute('href')
    items.append((title,price,link))

#print(items)

result=[]
for item in items:
    driver.get(item[2])

    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollheight)")
        time.sleep(3)
    
    comments = driver.find_elements(By.CSS_SELECTOR, "div[class ='']")
    for comment in comments:
        result.append((item[0], item[1], comment.text))
    
    

