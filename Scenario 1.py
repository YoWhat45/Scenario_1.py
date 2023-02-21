import pandas as pd
import numpy as np
import matplotlib as plot

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




