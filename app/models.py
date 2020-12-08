from datetime import datetime
from app import db


class City(db.Model):
    __tablename__ = 'Cities'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)


class Venue(db.Model):
    __tablename__ = 'Venues'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'))
    name = db.Column(db.String(100), index=True)


class Team(db.Model):
    __tablename__ = 'Teams'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    # venue_id = db.Column(db.Integer, db.ForeignKey('Venues.id'))
    name = db.Column(db.String(100), index=True, unique=True)
    # squad = db.relationship('Player', backref='team', lazy='dynamic')

    def __repr__(self):
        return '<Team {}>'.format(self.name)


class Player(db.Model):
    __tablename__ = 'Players'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    name = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Player {}>'.format(self.name)


class Official(db.Model):
    __tablename__ = 'Officials'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)


class Match(db.Model):
    __tablename__ = 'Matches'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Integer, db.ForeignKey('Cities.id'))
    venue = db.Column(db.Integer, db.ForeignKey('Venues.id'))
    umpire1 = db.Column(db.Integer, db.ForeignKey('Officials.id'))
    umpire2 = db.Column(db.Integer, db.ForeignKey('Officials.id'))
    team1 = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    team2 = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    toss_winner = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    winner = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    player_of_match = db.Column(db.String(100), index=True)
    toss_decision = db.Column(db.String(10), index=True)
    result = db.Column(db.String(10), index=True)
    win_by_runs = db.Column(db.Integer, index=True)
    win_by_wickets = db.Column(db.Integer, index=True)
    season = db.Column(db.Integer, index=True)
    date = db.Column(db.DateTime)
    dl_applied = db.Column(db.Integer, index=True)