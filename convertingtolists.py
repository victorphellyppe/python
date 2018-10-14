import pandas as pd
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
s = BeautifulSoup(r.content,'lxml')
t = s.find_all('table')[0]
df = pd.read_html(str(t))[0]
countries = df["COUNTRY"].tolist()
users = df["AMOUNT"].tolist()