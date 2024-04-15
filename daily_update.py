import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(filename='daily_update.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Database credentials and connection
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Set up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def execute_sql_file(sql_file_path):
    # Start a database session
    db_session = SessionLocal()
    try:
        with open(sql_file_path, 'r') as sql_file:
            # Read the file and split into individual commands, ignoring comment lines
            sql_commands = [command.strip() for command in sql_file.read().split(';') 
                            if command.strip() and not command.strip().startswith('--')]
            for command in sql_commands:
                if command:  # Ensuring the command is not empty
                    logging.info(f"Executing command: {command}")
                    result = db_session.execute(text(command))
                    # Fetch results if it's a SELECT statement
                    if command.lower().startswith('select'):
                        rows = result.fetchall()
                        logging.info(f"Query returned: {rows}")
            db_session.commit()
        logging.info("All queries executed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        db_session.rollback()
    finally:
        db_session.close()

if __name__ == "__main__":
    execute_sql_file('app/cron_jobs/queries.sql')
