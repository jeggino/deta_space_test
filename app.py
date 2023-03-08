# streamlit_app.py

import streamlit as st
import pandas as pd
import mysql.connector

# Reading data
toml_data = toml.load("secrets.toml")
# saving each credential into a variable
HOST_NAME = toml_data['mysql']['host']
DATABASE = toml_data['mysql']['database']
PASSWORD = toml_data['mysql']['password']
USER = toml_data['mysql']['user']
PORT = toml_data['mysql']['port']

# Using the variables we read from secrets.toml
mydb = mysql.connector.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

query = pd.read_sql('SELECT * FROM mytable;' , mydb)

st.dataframe(query)
