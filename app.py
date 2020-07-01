from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"


@app.route('/api/v1/ppg', methods=['GET'])
def getPlayerPPG(lastname):
	if request.method == 'GET':
		lastname = request.args['lastname']
        playerBox = getPlayerBox(lastname)
        ppg = sum(playerBox.get('PTS'))/len(playerBox.index)
	return ppg

def getPlayerIDFromFullName(fullName):
    return players.find_players_by_last_name(fullName)[0]['id']

def getPlayerBox(fullName):
    playerID = getPlayerIDFromFullName(fullName)
    boxScores = playergamelog.PlayerGameLog(season="2019", player_id=playerID, season_type_all_star="Regular Season").player_game_log.get_data_frame()
    return boxScores

def main():
    print(getPlayerPPG("Damian Lillard"))

if __name__ == "__main__":
    #main()
    app.debug=True
    app.run()