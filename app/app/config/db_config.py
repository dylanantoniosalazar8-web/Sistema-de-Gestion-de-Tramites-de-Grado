import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-morning-bird-ainibw75-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_8z0vqNMBHCih",
        dbname="neondb",
        sslmode="require"
    )