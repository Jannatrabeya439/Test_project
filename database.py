from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"

DATABASE_URL = "postgresql+psycopg2://training_w85w_user:pNpdcvMCSEplQsO6l7v7pbJ9JX9US44x@dpg-dbbfgum1egvs73fs9q70-a.virginia-postgres.render.com/training_w85w"

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autocommit = False, autoflush= False, bind= engine)
base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()