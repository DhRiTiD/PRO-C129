import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

page = requests.get(url)
soup = bs(page.text, 'html.parser')

star_table = soup.find_all('table')

print(star_table)

df=pd.read_html(str(star_table[7]))
df=pd.DataFrame(df[0])
print(df.head())

df.to_csv('brown_planet_data.csv')
