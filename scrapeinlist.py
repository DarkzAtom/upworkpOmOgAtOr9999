from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def scrapeitem(url):
    # url = "https://www.upwork.com/jobs/Coin-market-cap-span-class-highlight-scraping-span_~01a993c78a79304acf/"
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    # options.add_argument('--disable-gpu')
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.air3-card-sections.flex-1")))
        element_html = element.get_attribute('outerHTML')
    finally:
        driver.quit()

    soup = BeautifulSoup(element_html, 'html.parser')

    soup_of_features = soup.select_one('section:nth-child(3) > ul')


    payment = None

    project_type = None

    lis = soup_of_features.select('li')

    dict_of_features = {}

    for num, li in enumerate(lis):
        desc = li.find('div', class_='description').get_text(strip=True) if li.find('div', class_='description') is not None else li.find('strong').get_text(strip=True)

        stronk_tags = li.find_all('strong')
        if len(stronk_tags) > 1:
            stronk = '-'.join([tag.get_text(strip=True) for tag in stronk_tags])

        else:
            stronk = li.find('strong').get_text(strip=True) if li.find('strong').get_text(strip=True) != desc else None
        dict_of_features[f"{desc}"] = f"{stronk}"


    #payment section

    for key in dict_of_features:
        if "Hourly" or "Fixed-price" in key:
            if "$" in dict_of_features[key]:
                payment = dict_of_features[key]
            else:
                continue
        else:
            continue

    # type of the project section

    for key in dict_of_features:
        if "Project Type" in key:
            project_type = dict_of_features[key]
        else:
            continue

    # difficulty section

    for key in dict_of_features:
        if "Experience Level" in key:
            difficulty = dict_of_features[key]
        else:
            continue


    name = soup.select_one('h4.m-0').get_text(strip=True)
    opis = soup.select_one('p.text-body-sm').get_text()
    proposals = soup.select_one("li.ca-item span.value").get_text(strip=True)

    # снизу закоменченный код, который уже мне нахуй не нужен, но оставлю на память, потому что мне похуй

    # difficulty = soup.select_one('li:has(> .air3-icon.md [data-name="Layer 1"]) > strong').get_text()
    # print(soup)
    # print(dict_of_features)
    # print(name)
    # print(proposals)
    # print(difficulty)
    # print(project_type)
    # print(opis)
    # print(payment)
    # print(lis)


    item = {
        "Name" : name,
        "Payment" : payment,
        "Difficulty" : difficulty,
        "Proposals": proposals,
        "Project Type" : project_type,
        "Url" : url,
        "Description": opis
    }

    return item






