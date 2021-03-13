# coding: utf-8
import pandas as pd
import requests

url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv'


vax_data = pd.read_csv(url)


#separate into state's own csvs
def state_separate(data):
    for state in pd.unique(data['location']):
        data[data['location'] == state].to_csv("state_vax/" + state + ".csv", header=True,
                                               index=False)




#separate into ordered by date.
def date_separate(data):
    for date in pd.unique(data['date']):
        data[data['date'] == date].to_csv("date_vax/" + date + ".csv", header=True,
                                          index=False)





