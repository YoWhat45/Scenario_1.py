import pandas as pd
import matplotlib.pyplot as plt
import unittest

travel_df = pd.read_excel('./Project_File.xlsx')
travel_df.head()
travel_df.tail()
travel_df.shape

#Rename first column
travel_df.rename(columns={travel_df.columns[0]: "Year" }, inplace = True)

print(travel_df)

#Converting
travel_df = travel_df.astype('str')

print(travel_df.dtypes)

#Remove white space
travel_df.columns = travel_df.columns.str.strip()
#travel_df.index = travel_df.index.str.strip()

#Split Year and Month
travel_df[['Year', 'Month']] = travel_df['Year'].str.split(n=1, expand=True)

print(travel_df)

#Choosing other region
other_region_df = travel_df[["Year", "USA", "Canada", "Australia", "New Zealand", "Africa"]]

print(other_region_df)

#Choosing Years
other_region_df = other_region_df.astype('int')
print(other_region_df.dtypes)

other_region_years_df = other_region_df[(other_region_df['Year'] >= 2008) & (other_region_df['Year'] <= 2017)]

print(other_region_years_df)

#Sum amount of visitors
sum_travel_df = other_region_years_df.drop(columns=['Year'])
sum_travel_df = sum_travel_df.sum()
print(sum_travel_df)

#Plot Graph
plot_graph = {"USA": 4606203,
           "Canada": 870949,
           "Australia": 9798279,
           "New Zealand": 1155381,
           "Africa": 721871
          }

country_names = list(plot_graph.keys())
country_sum = list(plot_graph.values())

def addlabels(country_names,country_sum):
    for i in range(len(country_names)):
        plt.text(i,country_sum[i], country_sum[i])

plt.bar(x = country_names, height = country_sum)

plt.ticklabel_format(style='plain', axis='y')
addlabels(country_names, country_sum)
plt.title('Amount of Visitors from 2008 - 2017', size = 18)
plt.xlabel("Country Name", size = 12)
plt.ylabel("No. of Visitors", size = 12)

plt.show()

#Top 3 Countries
top_3_df = sum_travel_df
print(top_3_df.nlargest(3))

#Test Class
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
