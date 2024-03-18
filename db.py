import os

from google.cloud.sql.connector import Connector


from sqlalchemy import create_engine


def connect_with_connector():
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = os.environ['INSTANCE_CONNECTION_NAME']
    db_user = os.environ['DB_USER']  # e.g. 'my-db-user'
    db_pass = os.environ['DB_PASS']  # e.g. 'my-db-password'
    db_name = os.environ['DB_NAME']  # e.g. 'my-database'


    # initialize Cloud SQL Python Connector object
    connector = Connector()

    def getconn():
        conn = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    engine = create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    return engine