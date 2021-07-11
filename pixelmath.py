#from _typeshed import OpenTextModeReading
import csv 
import plotly_express as p
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('csv107.csv')
print(df.groupby('level')['attempt'].mean())

fig = go.Figure(go.Bar(
    x = df.groupby('level')['attempt'].mean(),
    y = ['level 1', 'level 2', 'level 3', 'level 4'],
    orientation = 'h'

))

fig.show()

