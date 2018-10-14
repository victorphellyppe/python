import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

r = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
s = BeautifulSoup(r.content,'lxml')
t = s.find_all('table')[0]
df = pd.read_html(str(t))
print(tabulate(df[0], headers='keys', tablefmt='psql'))