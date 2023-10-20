import psycopg2

# Set your database connection parameters
db_params = {
        "database": "<database>",
        "user": "<user>",
        "password": "<password>",
        "host": "<host>",
        "port": "<port>",
    }

def get_tables():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        cur.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
        table_names = [row[0] for row in cur.fetchall()]
        return table_names

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()


def change_table_owner(tables, new_owner):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        for table in tables:
            alter_owner_sql = f"ALTER TABLE {table} OWNER TO {new_owner};"
            cur.execute(alter_owner_sql)
            conn.commit()
            print(f"Ownership of table {table} has been changed to {new_owner}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()

