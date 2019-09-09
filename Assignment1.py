import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 6})

#===============================================================================
#===============================================================================

# General overview of the data
names = ["Income < 30.000", "Income 30-45.000", "Income 45-75.000", "Income 75-122.000", "Income >123.000", "1 car", "2 cars", "No car", "Roman catholic", "Protestant", "Other religion", "No religion", "Married", "Living together", "Other relation", "Singles", "Household without children", "Household with children", "High level education", "Medium level education", "Lower level education", "High status", "Entrepreneur", "Farmer", "Middle management", "Skilled labourers", "Unskilled labourers", "Number of houses", "Avg size household", "Avg age"]
data = pd.read_csv("MappingData.csv", names=names)
data.hist(figsize=[10, 10])
plt.title('My title')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()

#===============================================================================
#===============================================================================

# The y units are "percentage of a community", and the x unit is "number of cars"
# This shows the distribution of car ownership, and shows that it's most common for people to have one car,
# but there's a huge range (as can be seen by the whiskers and outliers)
# It's interesting to note what a huge range there is. Notice that in the "2 cars" section, there are a few
# outliers that imply there are zip codes where close to 100% of their residents have two cars, while the
# majority of communities have low percentages of households with two cars

df1 = pd.DataFrame({"No car":data["No car"], "1 car":data["1 car"], "2 cars":data["2 cars"]})
df1.plot(kind='box', subplots=False, figsize=[15, 5])
plt.show()

#===============================================================================
#===============================================================================

df2 = pd.DataFrame({"No car":data["No car"], "1 car":data["1 car"], "2 cars":data["2 cars"],
                   "High status":data["High status"], "Entrepreneur":data["Entrepreneur"],
                   "Farmer":data["Farmer"], "Middle management":data["Middle management"],
                   "Skilled labourers":data["Skilled labourers"],
                   "Unskilled labourers":data["Unskilled labourers"]})

subnames = ["No car", "1 car", "2 cars", "High status", "Entrepreneur", "Farmer", "Middle management", "Skilled labourers", "Unskilled labourers"]


correlations = df2.corr()
# plot correlation matrix
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(subnames)
ax.set_yticklabels(subnames)
plt.show()


# This graph is really interesting, as you can see a strong correlation between zip codes having high numbers
# of unskilled laborers and no car. One thing that I didn't expect, is that "high status" is more associated
# with having one car than being a skilled laborer is with any number of cars. However, this could mean that
# it's indicative that high status people will NOT have one car, so I need to do some more digging with that


#===============================================================================
#===============================================================================


q4 = data.loc[data["High status"] > 7.5]
q3 = data.loc[(data["High status"] > 5) & (data["High status"] < 7.5)]
q2 = data.loc[(data["High status"] > 2.5) & (data["High status"] < 5)]
q1 = data.loc[data["High status"] < 2.5]

dfHist = pd.DataFrame({'q1: No car':q1["No car"],'q2: No car':q2["No car"],'q3: No car':q3["No car"],'q4: No car':q4["No car"],
                      'q1: 1 car':q1["1 car"],'q2: 1 car':q2["1 car"],'q3: 1 car':q3["1 car"],'q4: 1 car':q4["1 car"],
                      'q1: 2 cars':q1["2 cars"],'q2: 2 cars':q2["2 cars"],'q3: 2 cars':q3["2 cars"],'q4: 2 cars':q4["2 cars"],})

df_norm = (dfHist - dfHist.mean()) / (dfHist.max() - dfHist.min())

hist = df_norm.hist(bins=10, figsize=(10, 10))
# Shows how cars are broken up in different income levels


#===============================================================================
#===============================================================================


df3 = pd.DataFrame({'q4: High status':q4["High status"],
                    'q4: No car':q4["No car"],
                    'q4: 1 car':q4["1 car"],
                    'q4: 2 cars':q4["2 cars"]})

subnames = ['q4: High status','q4: No car', 'q4: 1 car', 'q4: 2 cars']


correlations = df3.corr()
# plot correlation matrix
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,4,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(subnames)
ax.set_yticklabels(subnames)
plt.show()

# This is intersting because it suggests tht there's some kind of correlation between
# the number of wealthy people in a zip code and the number of 1 car households
# It requires more digging to be certain though


#===============================================================================
#===============================================================================


df4 = pd.DataFrame({'q4: No car':q4["No car"],
                    'q4: 1 car':q4["1 car"],
                    'q4: 2 cars':q4["2 cars"]})

fig= plt.figure(figsize=(6, 6))
plt.pcolor(df4)
plt.yticks(np.arange(0.5, len(df4.index), step=10), (df4.index)*10)
plt.xticks(np.arange(0.5, len(df4.columns), 1), df4.columns)
fig.colorbar(cax)
plt.show()

# This is a heatmap of the households that have x number of cars. As can be seen, 1 car households are common
# among "high status" households, and 2 car households are next. I would have thought that the number of cars
# would go up with status, but apparently not


#===============================================================================
#===============================================================================


df5 = pd.DataFrame({'q3: No car':q3["No car"],
                    'q3: 1 car':q3["1 car"],
                    'q3: 2 cars':q3["2 cars"]})

fig= plt.figure(figsize=(6, 6))
plt.pcolor(df5)
plt.yticks(np.arange(0.5, len(df5.index), step=10), (df5.index*10))
plt.xticks(np.arange(0.5, len(df5.columns), 1), df5.columns)
fig.colorbar(cax)
plt.show()

# By looking at this graph, we can see that there are also a lot of 1-car households in the q3 group of zip codes


#===============================================================================
#===============================================================================

df6 = pd.DataFrame({'q2: No car':q2["No car"],
                    'q2: 1 car':q2["1 car"],
                    'q2: 2 cars':q2["2 cars"]})

fig= plt.figure(figsize=(6, 6))
plt.pcolor(df6)
plt.yticks(np.arange(0.5, len(df6.index), step=100), (df6.index*100))
plt.xticks(np.arange(0.5, len(df6.columns), 1), df6.columns)
fig.colorbar(cax)
plt.show()


#===============================================================================
#===============================================================================


df7 = pd.DataFrame({'q1: No car':q1["No car"],
                    'q1: 1 car':q1["1 car"],
                    'q1: 2 cars':q1["2 cars"]})

fig= plt.figure(figsize=(6, 6))
plt.pcolor(df7)
plt.yticks(np.arange(0.5, len(df7.index), step=100), (df7.index*100))
plt.xticks(np.arange(0.5, len(df7.columns), 1), df7.columns)
fig.colorbar(cax)
plt.show()

# It looks like the number of cars gets less pronounced the less "high class" people are in a zip code, but
# it looks like the common trend is for there to be one car, with no-car households increasing as the number
# "high class" people goes down.
# The next step would be to see if income is related to the number of cars, and if being "high class" is
# related to income in this dataset, or if it's more of a social idea
