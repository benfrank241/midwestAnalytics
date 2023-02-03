from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file("C:/Users/benja/AppData/Roaming/gcloud/application_default_credentials.json")


app = Flask(__name__)
CORS(app)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='root2023',
                              host='34.29.90.189', database='baseball')

@app.route("/data", methods=["GET"])
def get_data():

    cursor = cnx.cursor()
    query = "SELECT * from baseball.offense"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    print(jsonify(data))
    return jsonify(data)

@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
