import pandas as pd, plotly
import  plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=False)

vax = pd.read_csv('vax.csv')

date = '2'

date_vax = vax[(vax['location'] == 'Alabama') & (vax['date'] == date)]

print(vax['date'])