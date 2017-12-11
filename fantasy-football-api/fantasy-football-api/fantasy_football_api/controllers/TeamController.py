from fantasy_football_api import app, db
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from fantasy_football_api.models.Team import Team

class TeamController(object):
    """description of class"""

    @app.route('/api/team', methods=['GET'])
    def getAllTeams():
        teams = db.session.query(Team).all()
        return jsonify(
                status=200,
                message='Got your teams',
                data=teams
            )


    @app.route('/api/team', methods=['POST'])
    def addTeam():
        data = request.get_json()
        name = data["name"]
        team = Team(
                name=name
            )
        db.session.add(team)
        db.session.commit()
        return jsonify(
                status=201,
                message='%s has been created' % (team.name),
                data=team
            )

