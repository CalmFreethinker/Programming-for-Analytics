import re
import pandas as pd 
import numpy as np 

#Question 1
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        #TO DO -- Complete the Code
        regex = re.compile(patterns)
        if regex.search(text) == None:
            return "No match found!"
        else:
            return "Found a match!"
print("text#1: " + text_match("The quick brown fox jumps over the lazy dog."))
print("text#2: " + text_match("Python_Exercises_1"))

#Question 2
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:", "".join(re.findall('[^\n\t\s]', text1))) #TO DO -- Complete the Code

#Question 3
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 
  
df = pd.DataFrame(dict) 

print(df.notnull())

#Question 4
df1 = pd.DataFrame({'lkey': ['faa', 'baa', 'bzz', 'faa'],
                    'value': [2, 3, 5, 7]})
df2 = pd.DataFrame({'rkey': ['faa', 'baa', 'bzz', 'faa'],
                    'value': [7, 8, 9, 10]})

print(df1.merge(df2, left_on='lkey', right_on='rkey'))

#Question 5
print("\n")
df = pd.read_csv('C:\\Users\\Charles\\jupyter_notebooks\\titanic.csv')
result = df.set_index(['sex', 'age']).reindex(columns=["Unnamed: 15","adult_male",
                                                       "alone","fare",
                                                       "parch","pclass",
                                                       "sibsp","survived"]).sum(level=('sex', 'age')).sort_index(level=('sex','age'))
print(result)
