def get_dataframe():
    import pandas as pd

    # load cleaned csv into dataframe
    return pd.read_csv('https://raw.githubusercontent.com/MilanMathew/machine_test_focaloid/main/lib/data/02_intermediate/matches.csv', parse_dates=['date'])
