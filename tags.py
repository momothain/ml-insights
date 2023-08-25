from dotenv import load_dotenv
import psycopg2
import os
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Tags:
    def __init__(self):
        load_dotenv()
        self.db_name = os.environ.get("POSTGRES_DB_NAME")
        self.host = os.environ.get("POSTGRES_HOST")
        self.port = os.environ.get("POSTGRES_PORT")
        self.user = os.environ.get("POSTGRES_USER")
        self.password = os.environ.get("POSTGRES_PASSWORD")
        self.postgres_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    # SQLAlchemy main function
    def main(self):
        engine = create_engine('postgresql://username:password@localhost/dbname')
        Session = sessionmaker(bind=engine)
        with Session() as session:
            # Perform database operations using the engine
            connection = engine.connect()
            result = connection.execute("SELECT * FROM users")
            for row in result:
                print(row)
    
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
                
                
    def psycopg2_main(self):
        with psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        ) as conn:
            with conn.cursor() as cursor:
                # Use the cursor for database operations
                cursor.execute("SELECT * FROM your_table_name")
                results = cursor.fetchall()
                for row in results:
                    print(row)
        print('Hellow World')

if __name__ == "__main__":
    t = Tags()
    t.main()
    
    
