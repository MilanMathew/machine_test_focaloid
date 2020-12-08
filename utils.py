def import_data_from_test_csv(db_session, db_uri):
    import pandas as pd
    from sqlalchemy import create_engine
    from app.models import City, Venue, Team, Official

    # read raw matches csv files
    df = pd.read_csv('test_files/matches.csv', parse_dates=['date'])

    # save cities and venues
    city_venue_df = df[['city', 'venue']].drop_duplicates()
    zip_city_venue = zip(city_venue_df['city'], city_venue_df['venue'])
    for cv in zip_city_venue:
        city = City()
        city.name = cv[0]
        db_session.add(city)
        db_session.commit()

        venue = Venue()
        venue.city_id = city.id
        venue.name = cv[1]
        db_session.add(venue)
        db_session.commit()
    
    # save teams
    team_set1 = set(df['team1'].drop_duplicates())
    team_set2 = set(df['team2'].drop_duplicates())
    all_teams = team_set1.union(team_set2)
    for team in all_teams:
        team_model = Team()
        team_model.name = team
        db_session.add(team_model)
    
    # save umpires
    umpire_set1 = set(df['umpire1'].drop_duplicates())
    umpire_set2 = set(df['umpire2'].drop_duplicates())
    all_umpires = umpire_set1.union(umpire_set2)
    for umpire in all_umpires:
        umpire_model = Official()
        umpire_model.name = umpire
        db_session.add(umpire_model)

    db_session.commit()

    # create a dict with key and name mappings for
    # cities, venues, teams and officials
    cities = db_session.query(City).all()
    cities_dict = {city.name: city.id for city in cities}
    venues = db_session.query(Venue).all()
    venues_dict = {venue.name: venue.id for venue in venues}
    teams = db_session.query(Team).all()
    teams_dict = {team.name: team.id for team in teams}
    officials = db_session.query(Official).all()
    officials_dict = {official.name: official.id for official in officials}

    # cities = df_matches['city'].drop_duplicates()
    # cities_dict = {x: y for y,x in enumerate(cities)}
    db_session.close()
    
    # change city, venue, team1, team2, umpire1, umpire2
    # names to their corresponding 'ids' from database
    df['city'] = df['city'].apply(lambda x: cities_dict[x])
    df['venue'] = df['venue'].apply(lambda x: venues_dict[x])
    df['team1'] = df['team1'].apply(lambda x: teams_dict[x])
    df['team2'] = df['team2'].apply(lambda x: teams_dict[x])
    df['toss_winner'] = df['toss_winner'].apply(lambda x: teams_dict[x])
    df['winner'] = df['winner'].apply(lambda x: teams_dict[x])
    df['umpire1'] = df['umpire1'].apply(lambda x: officials_dict[x])
    df['umpire2'] = df['umpire2'].apply(lambda x: officials_dict[x])

    # create sqlalchemy engine
    engine = create_engine(db_uri)

    # Insert dataframe into 'Matches' table
    df.to_sql('Matches', con=engine, if_exists='replace', index=False)
