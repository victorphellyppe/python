import pandas as pd
arquivo = 'C:\python\movies.xls'
movies = pd.read_excel(arquivo)
print(movies.head)