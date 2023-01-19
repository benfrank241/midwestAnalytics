from flask import Flask, render_template
import oAnalysis


app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('table.html', tables=[oAnalysis.frame.to_html(classes='data')], titles=oAnalysis.frame.columns.values)



if __name__ == '__main__':
    app.run(host='0.0.0.0')