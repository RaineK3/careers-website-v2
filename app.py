from flask import Flask, render_template,jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location' : 'Tamwe,Yangon',
#     'salary' : '40Lakhs-50Lakhs(Nego)'
#   },
#   {
#     'id': 2,
#     'title':'Data Scientist',
#     'location' : 'Downtown,Yangon',
#     'salary' : '40Lakhs-50Lakhs(Nego)'
#   },
#   {
#     'id': 3,
#     'title':'Backend Engineer',
#     'location' : 'Hlaing,Yangon',
#     'salary' : '50Lakh-70Lakh(Nego)'
#   },
#   {
#     'id': 4,
#     'title':'Fronted Engineer',
#     'location' : 'Sansaung,Yangon',
#     'salary' : '50Lakh-70Lakh(Nego)'
#   },
# ]



@app.route("/")
def hello_careers():
  JOBS = load_jobs_from_db()
  return render_template("home.html", jobs = JOBS, company_name = "IT")

@app.route('/api/jobs')
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  print(job)
  print(type(job))
  if not job:
    return "Not Found, 404"
  return render_template('jobpage.html', job = job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
