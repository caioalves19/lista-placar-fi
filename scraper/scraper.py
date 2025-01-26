from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from scraper.parser import parser_itens_placar


def iniciar_driver():
    try:
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return driver
    except Exception:
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print("Chrome detected and used.")
        return driver


def scrape_jogos(link):
    driver = iniciar_driver()
    driver.maximize_window()

    try:
        driver.get(link)
        sleep(3)
        itens_placar = driver.find_elements(By.XPATH,
                                            "//span[@class='scoreboard__tag'] | //h2[@class='subheader__title'] | "
                                            "//figcaption[@class='scoreboard__team-name'] | "
                                            "//figure["
                                            "@class='scoreboard__score-result']//span", )
        itens_placar = parser_itens_placar(itens_placar)
    finally:
        driver.quit()
    return itens_placar
