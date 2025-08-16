import os
import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "notesdb"),
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
        port=os.environ.get("POSTGRES_PORT", "5432")
    )
