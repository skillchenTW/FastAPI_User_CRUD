from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:F9n3v47t@localhost:3306/test')
meta = MetaData()
conn = engine.connect()