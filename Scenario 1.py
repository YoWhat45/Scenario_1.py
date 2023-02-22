import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

travel_df = pd.read_excel('./Project_File.xlsx', index_col=0)
travel_df.columns = travel_df.columns.str.strip()
travel_df.index = travel_df.index.str.strip()
travel_df.head()
travel_df.tail()
travel_df.shape

print(travel_df)

#Choosing other region
other_region_df = travel_df[['USA', 'Canada', 'Australia', 'New Zealand', 'Africa']]

print(other_region_df)

#Choosing Years
years_other_region_df = other_region_df["2008 Jan": "2017 Nov"]

print(years_other_region_df)

#Plotting
plot_graph = years_other_region_df

USA = plot_graph['USA']
Canada = plot_graph['Canada']
Australia = plot_graph['Australia']
NewZealand = plot_graph['New Zealand']
Africa = plot_graph['Africa']

plt.figure(facecolor = 'white', figsize = (8, 4))
plt.plot(USA)
plt.plot(Canada)
plt.plot(Australia)
plt.plot(NewZealand)
plt.plot(Africa)

plt.show()
#Test Class




