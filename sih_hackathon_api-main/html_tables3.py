import bs4 as bs
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

source = urllib.request.urlopen('https://pib.gov.in/PressReleasePage.aspx?PRID=1851326').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find_all('table')
df = pd.read_html(str(table))[0]

# df = df.iloc[7:-2, :]

print(df)

labels = df.iloc[2:, 2].values
data = df.iloc[2:, 3].values

data = data.astype(np.int)

print(data, labels)

plt.bar(labels, data, log=False)
plt.title("Fixation of Tariff Value for Edible Oils")
plt.xlabel("Description of goods")
plt.ylabel("Tariff value (US $Per Metric Tonne)")
plt.xticks(rotation = 20)
plt.show()