import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('mosquitos_data.csv')
df.head()
sns.set(style="ticks")
sns.boxplot(x="Treatment", y="Response", data=df)
plt.title=("Response Based")
plt.show()
df_grouped=df.groupby('Treatment')


print('\nThe mean value for mosquito bites with Beer treatment is: {}'.format(df_grouped.mean().loc['Beer', 'Response']))
print ('\nThe mean value for mosquito bites with Water treatment is: {}'.format(df_grouped.mean().loc['Water', 'Response']))
experiment_mean_diff = df_grouped.mean().loc['Beer', 'Response']-df_grouped.mean().loc['Water', 'Response']
print ('\nThis shows that the mean (average) of number of mosquito bites with Beer treatment is higher than water treatment by {}.'.format(experiment_mean_diff))

df_grouped.mean()

experiment_median_diff = df_grouped.median().loc['Beer', 'Response'] - df_grouped.median().loc['Water', 'Response']
print('\nThe median value for mosquito bites with Beer treatment is: {}'.format(df_grouped.median().loc['Beer', 'Response']))
print ('\nThe median value for mosquito bites with Water treatment is: {}'.format(df_grouped.median().loc['Water', 'Response']))
print ('\nThis shows that the middle number of mosquito bites is higher in Beer treatments by {}.'.format(experiment_median_diff))

df_grouped.median()
df_grouped.std()

# Data Simulation -- Plotting the Histogram of 50000 iterations -- Cosnidering the fact that the number of mosquito bites are random
import random
df['Treatment']='Beer'
list_index=[]
difference=[]
index=0
for iteration in range(1,50000):
    for i in range(0,18):
        index=random.randint(0,42)
        while index in list_index:
            index=random.randint(0,42)
        df.loc[index, 'Treatment']='Water'  # Shuffling Treatment
        list_index.append(index)
    df_grouped=df.groupby('Treatment')
    df_grouped.mean()
    difference.append(df_grouped.mean().loc['Beer', 'Response']-df_grouped.mean().loc['Water', 'Response'])
    df['Treatment']='Beer'
    list_index=[]
minimum= min(difference)
maximum = max(difference)
plt.hist(difference, bins=20)

# Calculating of obtaining the experiment outcome assuming no association between beer consumption
# Generating the Cumulative Distribution Function to measure the probabilities of different occurances
counts, bins, bars = plt.hist(difference, bins=20, density=True, cumulative=True)

# Calculating the Probability of obtaining the experiment outcome assuming no association between beer consumption and mosquito bites
import numpy as np
#Finding the edge of the bin that is greater than the experiment's difference in the mean
a= np.where(bins < experiment_mean_diff )
b=int(a[0][-1])
print('The bins edge is at: ', b)

print('The probability of obtaining the experiemnt outcome assuming no association with beer consumption is: \n', (1 - counts[b - 1]))
