import pandas as pd
import csv
import plotly.figure_factory as ff 

reader= pd.read_csv('data.csv')
figure= ff.create_distplot([reader['Avg Rating'].tolist()],['avg rating'], show_hist=False)
figure.show()