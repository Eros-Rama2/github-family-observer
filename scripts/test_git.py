from github import Github
from dotenv import load_dotenv

def initialize_main_repo():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('db/state.db')
    c = conn.cursor()

    # Drop the table if it exists (useful for development/testing)
    c.execute('DROP TABLE IF EXISTS state')

    # Create the table with the correct schema
    c.execute('''CREATE TABLE state (data TEXT)''')

    # Fetch and insert the initial state
    initial_state = fetch_initial_state_main_repo()
    # initial_state = {"branches": ["feat/great", "feat-bro", "feat-older", "final", "folder", "master"], "prs": {"4": "open", "3": "closed", "2": "open", "1": "closed"}}
    json_data = json.dumps(initial_state)

    # Insert the JSON data into the table
    c.execute('INSERT INTO state (data) VALUES (?)', (json_data,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

initialize_main_repo()
