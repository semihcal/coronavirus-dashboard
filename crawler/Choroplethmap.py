
import pandas as pd
import json
import geopandas as gpd
import matplotlib.pyplot as plt


with open('ohio.json', 'r') as f:
  data = json.load(f)


numofcases= data['daily'][0]['county_cases']
table = str.maketrans(dict.fromkeys("()"))
numofcases = numofcases.translate(table)
numofcases = numofcases.lstrip("Number of counties with cases: ")


x = numofcases.split(",")
y={}
for i in x:
    s = i.split()
    y.update({s[0].upper():int(s[1])})

df = pd.DataFrame(y.items(),columns= ['counties','number_of_cases'])

map_df = gpd.read_file('REFER_COUNTY.shx')


merged = map_df.set_index('COUNTY').join(df.set_index('counties'))
max_case = merged['number_of_cases'].max()


variable = 'number_of_cases'


ohmap = merged.plot(column=variable, cmap='Reds',  edgecolor='0.8', figsize=(8,5))
ohmap.axis('off')
ohmap.set_title('County Corona Cases in Ohio', fontdict={'fontsize': '25', 'fontweight' : '3'})
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=0, vmax=max_case))
sm._A = []
plt.colorbar(sm)
plt.show()


