from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='root2023',
                              host='34.29.90.189', database='baseball')

@app.route("/data", methods=["GET"])
def get_data():
    cursor = cnx.cursor()
    query = "SHOW COLUMNS FROM baseball.offense"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    print(jsonify(data))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
