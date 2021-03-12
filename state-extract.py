# coding: utf-8
import pandas as pd

vax_data = pd.read_csv("vax.csv")


def state_separate(data):
    for state in pd.unique(data['location']):
        data[data['location'] == state].to_csv("state_vax/" + state + ".csv", header=True,
                                               index=False)




# do it by date now instead of state

def date_separate(data):
    for date in pd.unique(data['date']):
        data[data['date'] == date].to_csv("date_vax/" + date + ".csv", header=True,
                                          index=False)


date_separate(vax_data)


