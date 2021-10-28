import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data108pt2.csv')

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Ratings"], show_hist = False)
fig.show()