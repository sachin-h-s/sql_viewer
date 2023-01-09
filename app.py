import streamlit as st
import sqlite3

st.title('SQLite Viewer')

# Connect to the database
conn = sqlite3.connect('database.db')

# Get a list of tables in the database
tables = [table[0] for table in conn.execute("SELECT name FROM sqlite_master WHERE type='table';")]

# Create a sidebar with a dropdown for selecting the table
selected_table = st.sidebar.selectbox('Select a table', tables)

# Retrieve the data from the selected table
data = pd.read_sql_query(f'SELECT * FROM {selected_table}', conn)

# Display the data as a table
st.table(data)

# Close the database connection
conn.close()
