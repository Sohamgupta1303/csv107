import csv 
import pandas as p
import plotly.graph_objects as pg

df = p.read_csv('csv107.csv')
sdf = df.loc[df['student_id']=='TRL_mno']

print(sdf.groupby('level') ['attempt'].mean())

fig = pg.Figure(pg.Bar(
    x = sdf.groupby('level') ['attempt'].mean(),
    y = ['level 1', 'level 2', 'level 3', 'level 4'],
    orientation = 'h'

))

fig.show()