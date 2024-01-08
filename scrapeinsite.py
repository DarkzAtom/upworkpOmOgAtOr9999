#данный скрипт автоматизирует поиск всех вакансий на апворке и публикует их мне в телеграм канале.
# Впоследствии, по хорошему, будет добавлен функционал автоматической отправки в искусственный интелект на обработку и выдачи ответа на вопрос, тяжелая ли эта задача на выполнение по мнению бота.



from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from scrapeinlist import scrapeitem

def scrapesite():

    url = "https://www.upwork.com/nx/search/jobs?client_hires=1-9,10-&payment_verified=1&q=scraping&sort=recency"

    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    # options.add_argument('--disable-gpu')
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.job-tile")))
        element_html = element.get_attribute('outerHTML')
    finally:
        driver.quit()




    soup = BeautifulSoup(element_html, 'html.parser')


    #site_item = site_items[0]

    id_soup = soup.find('article', class_='job-tile')
    id = id_soup.get('data-test-key')
    with open ('tempid.txt', 'r') as file:
        temp_id = file.read()
    if id == temp_id:
        sys.exit()
    else:
        with open ('tempid.txt', 'w') as file:
            file.write(str(id))

    urloftheitem_html = soup.select_one('a.up-n-link')
    urloftheitem = urloftheitem_html.get('href')

    url2item = "https://upwork.com" + urloftheitem

    item = scrapeitem(url2item)
    return item



    # print(item)


    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(str(soup))







