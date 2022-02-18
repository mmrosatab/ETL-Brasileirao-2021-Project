#!/usr/bin/env python
# coding: utf-8

#!pip3 install selenium
# before test this code, make download geckodriver and copy this file for /usr/local/bin
# sudo cp geckodriver /usr/local/bin

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
import time # it was necessary to trigger the click time on the buttons


# Globo esporte url's
athletes_url = "https://interativos.globoesporte.globo.com/estatisticas/atletas/"
teams_url = "https://interativos.globoesporte.globo.com/estatisticas/times/"


teams_titles = ['Gol marcado','Gols sofridos','Gols contra','Gols de falta',
              'Gol de pênalti','Gol de fora da área','Gols dentro da área','Finalização na trave',
              'Finalizações para fora','Faltas recebidas', 'Faltas cometidas',
             'Impedimentos','Cartões amarelos','Cartões vermelhos', 'Defesas difíceis',
             'Defesas de pênaltis', 'Roubadas de bola','Passes errados']


def extract_athletes_data():
    driver.get(athletes_url)
    driver.implicitly_wait(10)
    
def extract_teams_data():
    
    driver.get(teams_url)
    
    for title in teams_titles: 
        driver.find_element_by_xpath(f"//button[@data-title='{title}']").click()
        time.sleep(4)
        
    div_criterio = driver.find_element_by_xpath("//div[@class='criterio']")
    html_content = div_criterio.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    section_class_ranking_list = soup.find_all(class_='ranking')
#     artist_name_list_items = section_criterio_list.find_all('a')
    print(section_class_ranking_list)

    
#     for section in section_class_ranking_list:
        
#         name_csv = section.get('data-scoutnome')
        
#         print(name_csv)
#         print("********")
        
#         figure_list = section.get('figcaption')
        
#         for figure in figure_list:
#             team_name = figure.get(class_='ranking__nome')
#             print(team_name)
            
#             div_jogos = figure.get(class_='ranking__results--item ranking__results--jogos')
#             print(div_jogos)
            
#             div_total = figure.get(class_='ranking__results--item ranking__results--total')
#             print(div_total)
        

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
extract_teams_data()
driver.quit()
