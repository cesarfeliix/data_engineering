#scap data from websites

# if pd.read_html does not work, we can use pd.read_html using requests.
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
r = requests.get(url)
log('scapping initialize for table in the page: ' + url)

data_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
data = data_list[1]
log('table data was saved in a dataframe')

data.dropna(subset=['Bank name'], inplace=True) #This removes any blank values in the specified column
log('removed blank values in the specified column')
