from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
from google.cloud.sql.connector import Connector
import sqlalchemy

from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file("C:/Users/benja/AppData/Roaming/gcloud/application_default_credentials.json")


app = Flask(__name__)
CORS(app)


def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "sonic-solstice-376503:us-central1:analytics",
            "pymysql",
            user='root',
            password='root2023',
            database='baseball',
            credentials=creds
            )
        return conn
    
pool = sqlalchemy.create_engine(
"mysql+pymysql://",
creator=getconn,
)


@app.route("/data", methods=["GET"])
def get_data():

    with pool.connect() as cursor:
        # cursor = cnx.cursor()
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
