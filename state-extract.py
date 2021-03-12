# coding: utf-8
import pandas as pd

data = pd.read_csv("vax.csv")

states = pd.unique(data['location'])

for state in states:
    state_info = data[data['location']==state]
    state_info.to_csv("state_vax/"+state+".csv", header=True, index=False)
