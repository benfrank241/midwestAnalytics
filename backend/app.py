from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import sqlalchemy
# from google.oauth2.credentials import Credentials

# creds = Credentials.from_authorized_user_file("C:/Users/benja/AppData/Roaming/gcloud/application_default_credentials.json")


app = Flask(__name__)
CORS(app)
@app.route("/data", methods=["GET"])
def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of MySQL.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = os.environ["sonic-solstice-376503:us-central1:analytics"]  # e.g. 'project:region:instance'
    db_user = os.environ.get("benbart02", "")  # e.g. 'my-db-user'
    db_pass = os.environ["root2023"]  # e.g. 'my-db-password'
    db_name = os.environ["baseball"]  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector(ip_type)

    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            instance_connection_name,
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    print("success")

    return pool




# def get_data():
#     with conn() as cursor:
#         query = "SELECT * from baseball.offense"
#         cursor.execute(query)
#         data = cursor.fetchall()
#         cursor.close()
#         print(jsonify(data))
#         return jsonify(data)

@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
