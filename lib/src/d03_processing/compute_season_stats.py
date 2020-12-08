def list_seasons(df):
    return sorted([season for season in df['season'].drop_duplicates()])


def top_four_teams(df, season):
    from .sanitize import stringify_keys

    top_teams = df.loc[df['season'] == season, ['winner']].value_counts().head(4).to_dict()
    return stringify_keys(top_teams)


def team_with_max_toss_wins(df, season):
    top_team = df.loc[df['season'] == season, ['toss_winner']].describe().to_dict()
    return (top_team['toss_winner']['top'], top_team['toss_winner']['freq'])


def player_with_max_pom_wins(df, season):
    top_team = df.loc[df['season'] == season, ['player_of_match']].describe().to_dict()
    return (top_team['player_of_match']['top'], top_team['player_of_match']['freq'])


def team_with_max_wins(df, season):
    top_team = df.loc[df['season'] == season, ['winner']].describe().to_dict()
    return (top_team['winner']['top'], top_team['winner']['freq'])


def top_team_max_wins_venue(df, season):
    top_team = team_with_max_wins(df, season)[0]
    top_team_venue = df.loc[(df['season'] == season) & (df['winner'] == top_team), ['venue']].describe().to_dict()
    return (top_team_venue['venue']['top'], top_team_venue['venue']['freq'])


def win_toss_bat_first_percent(df, season):
    from .sanitize import formatted_decimal

    win_toss_and_bat_first_total = df.loc[(df['season'] == season) & (df['toss_decision'] == 'bat'), ['toss_winner']].value_counts().sum()
    total_matches = len(df.loc[df['season'] == season])
    return formatted_decimal(win_toss_and_bat_first_total * 100, total_matches)


def host_venue_max_matches(df, season):
    top_venue = df.loc[df['season'] == season, ['venue']].describe().to_dict()
    return (top_venue['venue']['top'], top_venue['venue']['freq'])


def team_victory_max_runs(df, season):
    row = df.iloc[df[df['season'] == season]['win_by_runs'].idxmax()].to_dict()
    return (row['winner'], row['win_by_runs'])
    # df.loc[df['win_by_runs'].idxmax()]
    # df.loc[df['season'] == 2008, ['winner', 'win_by_runs']]


def team_victory_max_wickets(df, season):
    row = df.iloc[df[df['season'] == season]['win_by_wickets'].idxmax()].to_dict()
    return (row['winner'], row['win_by_wickets'])


def win_toss_and_match_count(df, season):
    win_toss_and_match_total = df.loc[(df['season'] == season) & (df['winner'] == df['toss_winner']), ['winner', 'toss_winner']].value_counts().sum()
    return win_toss_and_match_total