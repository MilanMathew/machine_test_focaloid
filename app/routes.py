from app import app
from flask import render_template, request, jsonify
from .compute import get_seasons_list, generate_stats
from .models import Match


@app.route('/')
@app.route('/stats', methods=['GET', 'POST'])
def get_season_stats():
    season = int(request.form.get('selected_season', 2008))
    allowed_seasons = get_seasons_list()
    if season not in allowed_seasons:
        return jsonify("This season's data is not available. Try a value between 2008-2017.")

    result = generate_stats(season)
    result['selected_season'] = season
    result['seasons'] = allowed_seasons
    if app.config['TESTING']:
        return jsonify(result)
        
    return render_template('index.html', data=result)