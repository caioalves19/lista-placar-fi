from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep

from models.Campeonato import Campeonato
from models.Jogo import Jogo
from scraper.parser import parser_itens_placar


def scrape_jogos(link):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
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
