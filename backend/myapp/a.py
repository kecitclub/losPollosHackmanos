import psycopg2
from psycopg2 import OperationalError

conn = None  # Define conn as None before the try block
try:
    # Attempt to connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="192.168.127.42",
        database="wage",
        user="postgres",
        password="your_password"
    )
    print("Connection successful!")

    # Create a cursor object and execute a query
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table LIMIT 1;")  # Modify with a valid table name
    rows = cur.fetchall()

    if rows:
        print("Data retrieved successfully!")
        for row in rows:
            print(row)
    else:
        print("No data found.")

except OperationalError as e:
    print(f"Error: {e}")
    print("Connection failed!")

finally:
    # Close the connection if it was successfully established
    if conn:
        cur.close()
        conn.close()
        print("Connection closed.")
