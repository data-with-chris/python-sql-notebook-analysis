import sqlite3

import os

def connect_to_db() -> sqlite3.Connection | None:
    """
    Establishes a connection to the SQLite database.

    The database file is expected to be located at:
    <project_root>/database/warehouse.db

    Returns:
        sqlite3.Connection | None: A SQLite3 connection object if the connection
        is successful, otherwise None.

    Prints:
        The error message if a connection to the database could not be established.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    db_path = os.path.join(project_root, "database", "warehouse.db")
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(e)
        return None
