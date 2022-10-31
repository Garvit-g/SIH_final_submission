import bs4 as bs
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

source = urllib.request.urlopen('https://pib.gov.in/PressReleasePage.aspx?PRID=1853245').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find_all('table')
df = pd.read_html(str(table))[0]

df = df.iloc[7:-2, :]

print(df)

cols = df.columns
grouped = df.groupby(by=cols[1]).sum()

print(grouped)
labels = grouped.iloc[:-1:, 1].values[0:3]
data = grouped.index.values[0:3]

labels, data = data, labels

data = data.astype(np.int)
data /= 10e-9

print((data), (labels))

print(data)
print("labels")
print(labels)

colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()