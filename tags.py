from dotenv import load_dotenv
import psycopg2
import os
import difflib
# import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from app.models.advertiser import Advertiser



class Tags:
    def __init__(self):
        load_dotenv()
        self.db_name = os.environ.get("POSTGRES_DB_NAME")
        self.host = os.environ.get("POSTGRES_HOST")
        self.port = os.environ.get("POSTGRES_PORT")
        self.user = os.environ.get("POSTGRES_USER")
        quoted_password = quote_plus(os.environ.get("POSTGRES_PASSWORD"))
        self.password = quoted_password
        self.postgres_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        
        app = Flask(__name__)
        app.config['POSTGRES_URL'] = self.postgres_url
        db = SQLAlchemy(app)

    # SQLAlchemy main function
    def main(self):
        # print(self.db_name,self.host,self.port,self.user,self.password)
        print('URL:\n', self.postgres_url)
        
        engine = create_engine(self.postgres_url)
        Session = sessionmaker(bind=engine)
        # Create a session instance
        with Session() as session:
            advs = session.query(Advertiser).filter(Advertiser.platform_id == 2).all()
            for adv in advs:
                print(adv.id, adv.ad_id, adv.name)
            # Perform database operations using the session
            # result = session.execute(text("SELECT * FROM advertiser;"))
            # for row in result:
            #     print(row)    
    
    def read_queries(self):
        engine = create_engine(self.postgres_url)

        # Read the SQL queries from the .sql file
        with open('queries.sql', 'r') as file:
            sql_queries = file.read()

        # Execute the queries using SQLAlchemy
        with engine.connect() as connection:
            for query in sql_queries.split(';'):
                if query.strip():  # Skip empty lines
                    result = connection.execute(text(query))
                    for row in result:
                        print(row)
        
    def find_string_diff(string1, string2):
        diff = difflib.ndiff(string1.splitlines(), string2.splitlines())
        return '\n'.join(diff)

if __name__ == "__main__":
    t = Tags()
    t.main()
    
    
