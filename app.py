from service import AgendaService
from flask import Flask, request, render_template

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template('index.html')

@app.route("/agenda", methods=["POST"])
def create_agenda():
    agenda = AgendaService().create(request.form['raw_json'])
    return render_template('agenda.html', agenda=agenda)

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app