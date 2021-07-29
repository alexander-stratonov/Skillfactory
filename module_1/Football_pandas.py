import pandas as pd
football = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(football[football.Age == football.Age.min()].Reactions.mean())
    display(football[football.Age == football.Age.max()].Reactions.mean())
    display((football[football.Age == football.Age.max()].Reactions.mean()) 
            - (football[football.Age == football.Age.max()].Reactions.mean())