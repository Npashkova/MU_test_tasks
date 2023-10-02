import pandas as pd
import json

json_file = 'data/downloads.json'

with open(json_file, 'r') as file:
    data = json.load(file)
    estimates = data['estimates']
    print('The report about amount of null values in countries estimates')
    for element in estimates:
        country = element.get('countries')
        df = pd.DataFrame(country, columns=['country', 'value'])
        print(df.isnull().sum())
    print('The report about amount of null values in estimate_agg')
    estimates_agg = data['estimates_agg']
    df = pd.DataFrame.from_dict(estimates_agg, orient='index', columns=['estimates_agg'])
    print(df.isnull().sum())
    print('The report about amount of null values in countries')
    countries = data['countries']
    df = pd.DataFrame(countries)
    print(df.isnull().sum())
