# streamlit_app.py

import streamlit as st
import pandas as pd
import mysql.connector

# # Reading data
# toml_data = toml.load("secrets.toml")
# # saving each credential into a variable
# HOST_NAME = toml_data['mysql']['host']
# DATABASE = toml_data['mysql']['database']
# PASSWORD = toml_data['mysql']['password']
# USER = toml_data['mysql']['user']
# PORT = toml_data['mysql']['port']

# # Using the variables we read from secrets.toml
# mydb = mysql.connector.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

# query = pd.read_sql('SELECT * FROM mytable;' , mydb)

# st.dataframe(query)

# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
