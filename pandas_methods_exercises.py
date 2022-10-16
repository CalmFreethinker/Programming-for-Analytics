import numpy as np
import pandas as pd
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)

grouped =  df['data1'].groupby(df['key1'])#TO DO -- Compute groupby
print(grouped.mean()) #TO DO -- Compute mean

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())

#describe() is a pandas DataFrame method
#the variable df is index by column label and calls the
#the describe() method on it
#The output gives descriptive statistics that
#provides information on the central tendency,
#dispersion and shape of a dataset’s distribution and does not
#include NaN values.
#Count gives number of rows 
#mean gives the average 
#std gives standard deviation 
#min gives minimum value
#25% gives the 25th percentile
#50% gives the 50th percentile/ median
#75% gives the 75th percentile
#max gives the maximum value
df['data1'].describe()

#describe() is a pandas DataFrame method
#the variable df is index by column label and calls the
#the describe() method on it
#The output gives descriptive statistics that
#provides information on the central tendency,
#dispersion and shape of a dataset’s distribution and does not
#include NaN values.
#Count gives number of rows 
#mean gives the average 
#std gives standard deviation 
#min gives minimum value
#25% gives the 25th percentile
#50% gives the 50th percentile/ median
#75% gives the 75th percentile
#max gives the maximum value
df['data2'].describe()
