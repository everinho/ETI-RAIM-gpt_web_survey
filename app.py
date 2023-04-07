from flask import Flask, render_template, request
from database import full_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/form/end", methods=['get'])
def submit_page():   
  data = request.args

  full_db(data)
  return render_template('end.html', data=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
