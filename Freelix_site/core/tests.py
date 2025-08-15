from django.test import TestCase

# Create your tests here.

import psycopg2

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='myprojectuser',
        password='djangodatabase',  # Replace with your actual password 
        host='localhost',  # or your server IP
        port='5430'  # Default PostgreSQL port
    )
    print("Database connection successful")
    conn.close
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(f"Error: {e}") 