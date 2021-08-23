import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
small_df = df[df.columns[1:8]]
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(small_df)
s = df['FKAccuracy'].value_counts(bins=5)
display(s)
