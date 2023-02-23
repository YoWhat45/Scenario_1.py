import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest
import math

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

plt.plot(USA, label= 'USA')
plt.plot(Canada, label = 'Canada')
plt.plot(Australia, label = 'Australia')
plt.plot(NewZealand, label = 'New Zealand')
plt.plot(Africa, label = 'Africa')

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title('Other regions in years 2008 - 2017')
plt.xlabel('Month')
plt.ylabel('Country')
plt.legend()
plt.xticks(rotation = 90)
plt.margins(x=0, y=0)

plt.show()

#Top 3 countries in the region over a span of 10 years.
#top_countries_df = years_other_region_df

#top_countries_df['Sum'] = top_countries_df['USA'] + top_countries_df['Canada'] + top_countries_df['Australia']
#Test Class
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()





