def clean_null_values_in_csv():
    import pandas as pd

    # read raw matches csv files
    df = pd.read_csv('lib/data/01_raw/matches.csv', parse_dates=['date'])

    # drop column 'umpire3' since all its values are nulls
    df.drop(['umpire3'], axis=1, inplace=True)

    # drop matches which have no result (washed out due to rain)
    df.drop(300, inplace=True)
    df.drop(545, inplace=True)
    df.drop(570, inplace=True)

    # find rows which have nulls at either columns 'umpire1' and 'umpire2'
    null_row = df.loc[(df['umpire1'].isnull()) | (df['umpire2'].isnull())]

    # replace null umpires with correct names
    # data sourced from: https://cricclubs.com/IPL/fixtures.do?league=1&teamId=7&internalClubId=null&clubId=2447&fromDate=04/08/2017&toDate=04/08/2017
    umpire_cols = ['umpire1', 'umpire2']
    umpire_names = ['S Ravi', 'Virendra Sharma']
    for i in range(2):
        df.loc[df['id'] == int(null_row['id']), umpire_cols[i]] = umpire_names[i]

    # set 'Dubai' as the city for Dubai Int. Cricket Stadium
    df.loc[df['city'].isnull(), 'city'] = 'Dubai'

    # correct Pune Supergiant team name
    df.loc[df['team1'] == 'Rising Pune Supergiants', 'team1'] = 'Rising Pune Supergiant'
    df.loc[df['team2'] == 'Rising Pune Supergiants', 'team2'] = 'Rising Pune Supergiant'
    df.loc[df['toss_winner'] == 'Rising Pune Supergiants', 'toss_winner'] = 'Rising Pune Supergiant'
    df.loc[df['winner'] == 'Rising Pune Supergiants', 'winner'] = 'Rising Pune Supergiant'

    # finally save the cleaned csv
    df.to_csv('lib/data/02_intermediate/matches.csv', index=False)