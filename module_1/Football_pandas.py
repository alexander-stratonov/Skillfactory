import pandas as pd
football = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
composure_max = 0.9 * football.Composure.max()
reactions_max = 0.9 * football.Reactions.max()
print(composure_max)
print(reactions_max)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(football[football.Composure > composure_max
    & football.Reactions > reactions_max].Age.min())