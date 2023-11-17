from sqlalchemy import *

db_connection_string = "mysql+pymysql://root:raine@localhost/careers"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    row_dict = dict(row._asdict())
    result_dicts.append(row_dict)
    print(row_dict)
  print(result_dicts)

  # print("type(result)", type(result))
  # result_all = result.all()
  # print("type(result.all()):", type(result_all))
  
  # first_result = result_all[0]
  # first_result_dict = first_result._asdict.__dict__
  # print("type(first_result):", type(first_result))
  # print("type(first_result_dict):", type(first_result_dict))
  # print(first_result)
  # print(first_result_dict)
 
