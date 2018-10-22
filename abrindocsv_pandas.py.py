##abrindo csv com pandas
import pandas as pd
df = pd.read_csv('VendasTesouroDireto.csv',sep=';',encoding='ISO-8859-1')
print(df)
