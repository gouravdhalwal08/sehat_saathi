import sqlite3
import pandas as pd

DB_FILE = "reminders.db"

def init_db():
    """Initializes the database and creates the reminders table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                child_name TEXT NOT NULL,
                vaccine_name TEXT NOT NULL,
                due_date DATE NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def add_reminder(child_name, vaccine_name, due_date):
    """Adds a new vaccination reminder to the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reminders (child_name, vaccine_name, due_date) VALUES (?, ?, ?)",
            (child_name, vaccine_name, due_date)
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error on add: {e}")
    finally:
        if conn:
            conn.close()

def get_reminders_as_df():
    """Fetches all reminders and returns them as a Pandas DataFrame."""
    try:
        conn = sqlite3.connect(DB_FILE)
        # Using pandas to read SQL query directly into a DataFrame
        df = pd.read_sql_query("SELECT * FROM reminders ORDER BY due_date ASC", conn)
        return df
    except sqlite3.Error as e:
        print(f"Database error on fetch: {e}")
        return pd.DataFrame() # Return empty dataframe on error
    finally:
        if conn:
            conn.close()

def update_reminder(df: pd.DataFrame):
    """Updates the database based on changes in the DataFrame."""
    try:
        conn = sqlite3.connect(DB_FILE)
        df.to_sql('reminders', conn, if_exists='replace', index=False)
    except sqlite3.Error as e:
        print(f"Database error on update: {e}")
    finally:
        if conn:
            conn.close()