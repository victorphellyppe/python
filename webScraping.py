import pandas as pd
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
s = BeautifulSoup(r.content,'lxml')
t = s.find_all('table')[0]
df = pd.read_html(str(t))
print(df[0].to_json(orient='records'))
