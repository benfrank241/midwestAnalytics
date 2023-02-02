from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/data", methods=["GET"])
def get_data():

    cnx = mysql.connector.connect(user='root', password='root2023',
                              host='34.29.90.189', database='baseball')

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
