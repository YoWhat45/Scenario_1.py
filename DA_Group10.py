import pandas as pd
import matplotlib.pyplot as plt

travel_df = pd.read_excel('./Project_File.xlsx')

#View the new dataframe
print(travel_df.head())
print(travel_df.tail())
print(travel_df.shape)

#Rename first column
travel_df.rename(columns={travel_df.columns[0]: "Year" }, inplace = True)

print(travel_df)

#Remove white space
travel_df.columns = travel_df.columns.str.strip()
#travel_df.index = travel_df.index.str.strip()

#Converting
travel_df = travel_df.astype('str')

print(travel_df.dtypes)

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
plot_graph = sum_travel_df.sort_values(ascending=False)

ax = plot_graph.plot(kind = 'bar', title = 'Amount of Visitors from 2008 - 2017', color = 'magenta')
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation = 0)
plt.xlabel("Country Name", size = 14)
plt.ylabel("No. of Visitors", rotation = 0, size = 14)

plt.show()
#New
#Top 3 Countries
top_3_df = sum_travel_df
print(top_3_df.nlargest(3))
