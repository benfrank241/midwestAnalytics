from flask import Flask, render_template
import test


app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('table.html', tables=[test.frame.to_html(classes='data')], titles=test.frame.columns.values)



if __name__ == '__main__':
    app.run(host='0.0.0.0')