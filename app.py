from flask import Flask, render_template,jsonify
from database import engine

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location' : 'Tamwe,Yangon',
    'salary' : '40Lakhs-50Lakhs(Nego)'
  },
  {
    'id': 2,
    'title':'Data Scientist',
    'location' : 'Downtown,Yangon',
    'salary' : '40Lakhs-50Lakhs(Nego)'
  },
  {
    'id': 3,
    'title':'Backend Engineer',
    'location' : 'Hlaing,Yangon',
    'salary' : '50Lakh-70Lakh(Nego)'
  },
  {
    'id': 4,
    'title':'Fronted Engineer',
    'location' : 'Sansaung,Yangon',
    'salary' : '50Lakh-70Lakh(Nego)'
  },
]

def load_jobs_from_db():
  with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    row_dict = dict(row._asdict())
    result_dicts.append(row_dict)

@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS, company_name = "Jovian")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
