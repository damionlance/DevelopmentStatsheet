from main.dataQuery import *
from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route('/api/v1/ppg', methods=['GET'])
def getPlayerPPG(firstName=None, lastName=None):
    if request.method == 'GET':
        if 'lastName' in request.args and 'firstName' in request.args:
            lastName = request.args['lastName']
            firstName = request.args['firstName']
        fullName = firstName + " " + lastName
        playerBox = getPlayerBox(fullName)
        ppg = sum(playerBox.get('PTS'))/len(playerBox.index)
    else:
        ppg = 0
    return str(ppg)

@app.route('/api/v1/report/games', methods=['GET'])
def getReport():
    if request.method == 'GET':
        if 'firstName' in request.args and 'lastName' in request.args:
            lastName = request.args['lastName']
            firstName = request.args['firstName']
        fullName = firstName + " " + lastName
        playerBoxSeason = getPlayerBox(fullName)
        if 'numGames' in request.args:
            numGames = int(request.args['numGames'])
        else:
            numGames = 1
        playerBoxLastNGames = playerBoxSeason.head(numGames)
        playerBoxSeason = playerBoxSeason.tail(len(playerBoxSeason.index)-numGames)
        report = generateReport(playerBoxSeason, playerBoxLastNGames, fullName)
    else:
        return
    return report

if __name__ == "__main__":
    app.debug=True
    app.run()