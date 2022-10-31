import bs4 as bs
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
https://pib.gov.in/PressReleasePage.aspx?PRID=1854235
"""

source = urllib.request.urlopen('https://pib.gov.in/PressReleasePage.aspx?PRID=1854235').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find_all('table')
df = pd.read_html(str(table))[0]

cols = df.columns

df.iloc[:, 1] = df.iloc[:, 1].apply(pd.to_numeric, errors='coerce')
df = df.iloc[1:, :]

data = df.iloc[:, 1].values
labels =  df.iloc[:, 0].values

plt.bar(labels, data, log=True)
plt.title("COVID-19 Vaccine Availability 25th Aug 2022")
plt.xlabel("Vaccine Doses")
plt.ylabel("Vaccines as on 25th Aug 2022")
plt.show()