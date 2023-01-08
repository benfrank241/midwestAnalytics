from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import data


app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('table.html',  tables=[data.stat.to_html(classes='data')], titles=data.stat.columns.values)



if __name__ == '__main__':
    app.run(host='0.0.0.0')