from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd

def getPlayerIDFromFullName(fullName):
    return players.find_players_by_full_name(fullName)[0]['id']

def getPlayerBox(fullName):
    playerID = getPlayerIDFromFullName(fullName)
    boxScores = playergamelog.PlayerGameLog(season="2019", player_id=playerID, season_type_all_star="Regular Season").player_game_log.get_data_frame()
    return boxScores
