#get btc-brl historical data from last month


#author: Cesar R. Felix
#created: 2022-09-22
#subject: data_engineering


#call for libraries
import requests
import pandas as pd

#extract
url = "https://br.investing.com/crypto/bitcoin/btc-brl-historical-data"

request = requests.get(url)
data_list = pd.read_html(request.text)
data = data_list[1]

#transform
data.columns = ['date', 'closure', 'opening', 'maximum', 'minimum', 'volume','variance']
data['variance'] = data['variance'].map(lambda x: x.lstrip('+').rstrip('%'))
data['variance'] = data['variance'].astype(float)
data['variance'] = data['variance'].div(100)

#load
file_name = 'btc_last_month.csv'
data.to_csv(file_name, index=False, encoding='utf-8')

#download
from google.colab import files
files.download(file_name)
