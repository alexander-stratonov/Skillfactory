import pandas as pd
from IPython.display import display
#df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
small_df = df[df.columns[1:8]].head(25)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(small_df)
s = small_df['Nationality'].value_counts()
s_df = s.reset_index()
s_df.columns = ['Nationality','Players Count']
display(s_df)