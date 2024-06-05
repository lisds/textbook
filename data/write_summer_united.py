#!/usr/bin/env python3
""" Write summer_united.csv file from source flight.csv file

See below for source file.
"""

import pandas as pd
pd.set_option('mode.copy_on_write', True)

# Set path to flights.csv from archive at
# https://www.kaggle.com/datasets/usdot/flight-delays
df = pd.read_csv('flights.csv')

summer_united = df[
    (df['YEAR'] == 2015) &  # In fact this is true of all rows.
    df['MONTH'].isin([6, 7, 8]) &  # Summer
    (df['ORIGIN_AIRPORT'] == 'SFO') &
    (df['AIRLINE'] == 'UA')
]

summer_united['Date'] = (df['MONTH'].astype(str) + '/' +
                         df['DAY'].astype(str) + '/15')

summer_united = summer_united.sort_values(
    ['MONTH', 'DAY', 'FLIGHT_NUMBER'])

# Departure NA values only for cancellations.
# Plan to drop these.
assert (summer_united[
    summer_united['DEPARTURE_DELAY'].isna()
]['CANCELLED'].all())

renames = {'FLIGHT_NUMBER': 'Flight Number',
           'DESTINATION_AIRPORT': 'Destination',
           'DEPARTURE_DELAY': 'Delay'}

renamed = summer_united[['Date'] + list(renames)].rename(renames, axis=1)
dropped = renamed[~renamed['Delay'].isna()]  # Drop NA delay.
dropped['Delay'] = dropped['Delay'].astype(int)
out_df = dropped.reset_index(drop=True)

out_df.to_csv('summer_united.csv', index=False)
