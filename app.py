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

if __name__ == "__main__":
    app.debug=True
    app.run()