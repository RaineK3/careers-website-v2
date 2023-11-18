from sqlalchemy import *

db_connection_string = "mysql+pymysql://root:raine@localhost/careers"
engine = create_engine(db_connection_string)

  # print("type(result)", type(result))
  # result_all = result.all()
  # print("type(result.all()):", type(result_all))
  
  # first_result = result_all[0]
  # first_result_dict = first_result._asdict.__dict__
  # print("type(first_result):", type(first_result))
  # print("type(first_result_dict):", type(first_result_dict))
  # print(first_result)
  # print(first_result_dict)
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      row_dict = dict(row._asdict())
      jobs.append(row_dict)
    return jobs
  

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"select * from jobs where id = {id}"),
    )

    rows = result.all()
    if len(rows) == 0:
      return None
    else: 
      return rows[0]
      # jobs={}
      # for row in rows:
      #   row_dict = dict(row._asdict())
      #   jobs.append(row_dict)
      # return jobs

def add_applicatin_to_db(id,data):
  print(id)
  print(type(id))
  print(data)
  print(data['name'])
  print(data['email'])
  print(data['url'])
  print(data['education'])  
  print(data['work_exp'])  
  print(data['resume'])  
  with engine.connect() as conn:
    # query = text(f"INSERT INTO applications (job_id, username, email, linkedin_url, education, work_experience, resume_url) VALUES ({id}, {data['name']}, {data['email']}, {data['url']},{data['education']}, {data['work_exp']}, {data['resume']})")

    query = text("INSERT INTO applications (job_id, username, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"%(id, data['name'], data['email'], data['url'], data['education'],data['work_exp'], data['resume']))

    print(query)

    conn.execute(query)

    # conn.execute(query,  
    #              username=data['name'],
    #              email=data['email'],
    #              linkedin_url=data['url'],
    #              education=data['education'],
    #              work_experience=data['work_exp'],
    #              resume_url=data['resume'])

  # conn.execute(text(f"insert into applications (job_id, username, email, linkedin_url, education, work_experience, resume_url) values ({job_id}, {data['name']}, {data['email']}, {data['url']}, {data['education']}, {data['work_exp']}, {data['resume']})"))