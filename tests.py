import os
import unittest

from config import basedir
from app import app, db
from utils import import_data_from_test_csv


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
        import_data_from_test_csv(db.session, app.config['SQLALCHEMY_DATABASE_URI'])

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_stats(self):
        res = self.app.post('/stats', data=dict(selected_season=2012))
        data = res.json
        self.assertEqual(data['selected_season'], 2012)

        top_four_teams = data['top_four_teams_on_wins']
        self.assertEqual(len(top_four_teams), 4)
        self.assertEqual(top_four_teams[0][0], 'Kolkata Knight Riders')
        self.assertEqual(top_four_teams[0][1], 4)
        self.assertEqual(top_four_teams[1][0], 'Mumbai Indians')
        self.assertEqual(top_four_teams[1][1], 3)
        self.assertEqual(top_four_teams[2][0], 'Royal Challengers Bangalore')
        self.assertEqual(top_four_teams[2][1], 2)
        self.assertEqual(top_four_teams[3][0], 'Rajasthan Royals')
        self.assertEqual(top_four_teams[3][1], 1)

        self.assertEqual(data['team_with_max_toss_wins'][0], 'Delhi Daredevils')
        self.assertEqual(data['team_with_max_toss_wins'][1], 3)

        self.assertEqual(data['player_with_max_pom_wins'][0], 'DR Smith')
        self.assertEqual(data['player_with_max_pom_wins'][1], 2)

        self.assertEqual(data['team_with_max_wins'][0], 'Kolkata Knight Riders')
        self.assertEqual(data['team_with_max_wins'][1], 4)

        self.assertEqual(data['top_team_max_wins_venue'][0], 'MA Chidambaram Stadium, Chepauk')
        self.assertEqual(data['top_team_max_wins_venue'][1], 2)

        self.assertEqual(data['win_toss_bat_first_percent'], 53.8)    # 7 out of 13

        self.assertEqual(data['host_venue_max_matches'][0], 'MA Chidambaram Stadium, Chepauk')
        self.assertEqual(data['host_venue_max_matches'][1], 4)

        self.assertEqual(data['team_victory_max_runs'][0], 'Chennai Super Kings')
        self.assertEqual(data['team_victory_max_runs'][1], 86)

        self.assertEqual(data['team_victory_max_wickets'][0], 'Mumbai Indians')
        self.assertEqual(data['team_victory_max_wickets'][1], 10)

        self.assertEqual(data['win_toss_and_match_count'], 3)


if __name__ == '__main__':
    unittest.main()