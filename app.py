from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

# @app.route("/end")
# def final_page():   
#     return render_template('end.html')

# @app.route("/form/end", methods=['get'])
# def submit_page():   
#   data = request.form

#   add_answers_to_db(data)
#   return render_template('end.html', data=data)

@app.route("/form/end", methods=['get'])
def poll_submit():
  data = request.args
  return render_template('end.html', answers = data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
