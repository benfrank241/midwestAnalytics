from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='root2023',
                              host='localhost', database='baseball')

@app.route("/data", methods=["GET"])
def get_data():
    cursor = cnx.cursor()
    query = "SELECT * FROM offense"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
