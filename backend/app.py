from flask import Flask, jsonify, request
from flask_cors import CORS
import ssl
import mysql.connector

app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def conn():
    cnx = mysql.connector.connect( host="34.29.90.189", user="ben", password="root2023", database="baseball" )

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM baseball.offense")

    data = cursor.fetchall()
    return jsonify(data)
    

@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)

#TODO: add app ip to accepted connections

