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

def generateReport(playerBoxSeason, playerBoxLastNGames, fullName):
    report = f"""
    {fullName}:

    In the last {len(playerBoxLastNGames.index)} games, {fullName} has averaged {sum(playerBoxLastNGames.get('PTS'))/len(playerBoxLastNGames.index)} points per game.
    His highest point mark being {playerBoxLastNGames.get('PTS').max()} and his lowest being {playerBoxLastNGames.get('PTS').min()}. 
    This average is {"higher" if sum(playerBoxLastNGames.get('PTS'))/len(playerBoxLastNGames.index) > sum(playerBoxSeason.get('PTS'))/len(playerBoxSeason.index) else "lower"}
    than {fullName}'s season average of {sum(playerBoxSeason.get('PTS'))/len(playerBoxSeason.index)}
    
    """
    return report
