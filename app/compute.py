import json
import numpy as np

from . import db
from lib.src.d03_processing.compute_season_stats import *


def custom_json_encoder(obj):
    # courtesy: https://rymc.io/blog/2019/using-a-custom-jsonencoder-for-pandas-and-numpy/

    if isinstance(obj, np.generic):
        return np.asscalar(obj)


def get_season_dataframe(season=None):
    import pandas as pd

    sql = """
        select M.id, M.season, M.win_by_runs, M.win_by_wickets, M.player_of_match, 
        T1.name as team1, T2.name as team2, TTossWin.name as toss_winner, M.toss_decision as toss_decision,
        TWin.name as winner, V.name as venue

        from "Matches" M
        left join "Teams" T1 on T1.id = M.team1
        left join "Teams" T2 on T2.id = M.team2
        left join "Teams" TWin on TWin.id = M.winner
        left join "Teams" TTossWin on TTossWin.id = M.toss_winner
        left join "Venues" V on V.id = M.venue
        left join "Cities" C on C.id = M.city

        {where_query}
        ;
    """
    if season is not None:
        where_query = "where M.season = {season}".format(season=season)
    else:
        where_query = ""

    df = pd.read_sql(sql.format(where_query=where_query), con=db.session.get_bind())
    return df


def get_seasons_list():
    df = get_season_dataframe()
    return list_seasons(df)


def generate_stats(season):
    result = {}
    df = get_season_dataframe(season=season)

    # mandatory stats
    result['top_four_teams_on_wins'] = top_four_teams(df, season)
    result['team_with_max_toss_wins'] = team_with_max_toss_wins(df, season)
    result['player_with_max_pom_wins'] = player_with_max_pom_wins(df, season)
    result['team_with_max_wins'] = team_with_max_wins(df, season)
    result['top_team_max_wins_venue'] = top_team_max_wins_venue(df, season)
    result['win_toss_bat_first_percent'] = win_toss_bat_first_percent(df, season)
    result['host_venue_max_matches'] = host_venue_max_matches(df, season)
    result['team_victory_max_runs'] = team_victory_max_runs(df, season)

    # optional stats
    result['team_victory_max_wickets'] = team_victory_max_wickets(df, season)
    result['win_toss_and_match_count'] = win_toss_and_match_count(df, season)
    return json.loads(json.dumps(result, default=custom_json_encoder))