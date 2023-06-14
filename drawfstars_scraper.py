from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
        soup = BeautifulSoup(browser.page_source, "html.parser")
        
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        table_body = bright_star_table.find('tbody')

        table_rows = table_body.find_all('tr')

        for row in table_rows:
            table_cols = row.find_all('td')
            
            temp_list = []

            for col_data in table_cols:
                data = col_data.text.strip()

                temp_list.append(data)
            
            ch = 0
            for i in temp_list:
                if i == '':
                    i = 0.0
                    ch = 1
            if ch != 0:
                scraped_data.append(temp_list)
           
scrape()

stars_data = []

for i in range(0,len(scraped_data)):
     
    Star_names = scraped_data[i][0]
    Distance = scraped_data[i][5]
    Mass = float(scraped_data[i][8])*0.000954588
    Radius = scraped_data[i][9]


    required_data = [Star_names, Distance, Mass, Radius]
    stars_data.append(required_data)

print(stars_data)


headers = ['Star_name','Distance','Mass','Radius']  


df = pd.DataFrame(stars_data, columns=headers)


df.to_csv('dwarf_stars_data.csv',index=True, index_label="id")
