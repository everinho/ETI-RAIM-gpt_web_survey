from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://9ylf6aw63keny1r5bggz:pscale_pw_ImaonUBaSUlGQEkXGj4MsD4lfcyO6FAhkEYSmEEAgDk@aws.connect.psdb.cloud/gptdatabase?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }

)

with engine.connect() as conn:
  result = conn.execute(text("select * from users"))
  print(result.all())
