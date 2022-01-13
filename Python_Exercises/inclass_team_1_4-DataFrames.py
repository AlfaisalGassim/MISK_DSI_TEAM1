#importing relevant libraries
#%%
import pandas as pd
import numpy as np

# pandas DataFrames - Data containers, pt 4

# Get a DataFrame when impoting a file

# Or from a dict:
foo1 = [True, False, False, True, True, False]
foo2 = ["Liver", "Brain", "Testes", "Muscle", "Intestine", "Heart"]
foo3 = [13, 88, 1233, 55, 233, 18]

# Collect list into a dataframe
foo_df = pd.DataFrame({'healthy': foo1, 'tissue': foo2, 'quantity': foo3})
foo_df
type(foo_df)

# Or from a list of keys and values:
list_names = ['healthy', 'tissue', 'quantity']
# A list of lists
list_cols = [foo1, foo2, foo3]
# zip put the key/value pairs together
pd.DataFrame(dict(zip(list_names, list_cols)))

# Access information by:
# Name (here)
# Position (later, indexing)

# columns
foo_df.columns
# rows
foo_df.index

foo_df['healthy'] # Series
type(foo_df['healthy'])

foo_df[['healthy']] # DataFrame
type(foo_df[['healthy']])

foo_df.healthy # a Series

foo_df[['quantity', 'healthy']] # DataFrame

# each column is a Series
# DataFrames are build upon np.arrays
# i.e. Series can only be ONE type!

foo_df.info()

quantity_list = foo3.copy()
# quantity_list.mean() # no!
np.mean(quantity_list) # yes :)
# quantity_list/100 # no!

quantity_array = np.array(foo3)
quantity_array.mean()
quantity_array/100
quantity_array.astype("str")
# quantity_array.name # no!

quantity_Series = foo_df['quantity']
quantity_Series.mean()
quantity_Series/100
quantity_Series.astype("str")
quantity_Series.name

test_Series = pd.Series(quantity_array)
test_Series.name = "hello"
test_Series

#4.5
#%%
foo_df_2 = foo_df.copy()
foo_df_2.columns = ['A', 'B', 'C']
foo_df_2.index = ['H', 'I', 'J', 'K', 'L', 'M']
print(foo_df_2) # The copy

'''
Exercise 5.1 Using foo_df, what commands would I use to get:
The 2nd to 3rd rows?
The last 2 rows?
A random row in foo_df?
From the 4th to the last row? But without hard-coding, i.e. regardless of how many rows my data frame contains
'''
# %%
foo_df.iloc[[1,2]]

#%%
foo_df.iloc[[-2,-1]]
# %%
foo_df.iloc[[-4]]
# %%
foo_df.sample()

'''
Exercise 5.2 List all the possible objects we can use inside iloc[]

e.g. When can we use: - Integers? - Floats? - Characters? 
- A heterogenous list? - A homogenous list?
Although we typically just use seq[start:end], 
the complete notation is seq[start:end:step]. 
The step operation tells how at what interval to sample from the data set. We can reverse the sequence using [::-1]
'''
'''
- Integer. 
- list of integers.
- array of integers.
- sliced object with integers.
- boolen array.

'''
#%%



'''
Exercise 5.4 Subset for boolean data:

Only “healthy” samples.
Only “unhealthy” samples.
'''
#%%
foo_h = foo_df[(foo_df.healthy == True)]
print(foo_h)

#%%
foo_uh = foo_df[(foo_df.healthy == False)]
print(foo_uh)
'''
Exercise 5.5 Subset for numerical data:

Only low quantity samples, those below 100.
Quantity between 100 and 1000,
Quantity below 100 and beyond 1000.
'''
#%%
foo_under_100 = foo_df[(foo_df.quantity < 100)]
print(foo_under_100)

#%%
foo_under_100_1000 = foo_df[(foo_df.quantity >= 100) & (foo_df.quantity <= 1000)]
print(foo_under_100_1000)

#%%
foo_under_100_or_1000 = foo_df[(foo_df.quantity <= 100) | (foo_df.quantity >= 1000)]
print(foo_under_100_or_1000)

'''

Exercise 5.6 Subset for strings:

Only “heart” samples.
“Heart” and “liver” samples
Everything except “intestines”
'''
# %%
foo_df_heart = foo_df[(foo_df.tissue == "Heart")]
print(foo_df_heart)
# %%

foo_df_heart_liver = foo_df[(foo_df.tissue == "Heart") | (foo_df.tissue == "Liver")]
print(foo_df_heart_liver)
# %%
foo_df_Intestine = foo_df[(foo_df.tissue != "Intestine")]
print(foo_df_Intestine)

# %%
