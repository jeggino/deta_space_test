# streamlit_app.py

import streamlit as st
import pandas as pd
import mysql.connector
import toml

# # Reading data
# toml_data = toml.load(".streamlit/secrets.toml")
# # saving each credential into a variable
# HOST_NAME = toml_data['mysql']['host']
# DATABASE = toml_data['mysql']['database']
# PASSWORD = toml_data['mysql']['password']
# USER = toml_data['mysql']['user']
# PORT = toml_data['mysql']['port']

# st.write(PASSWORD)
# # Using the variables we read from secrets.toml
# mydb = mysql.connector.connect(host=HOST_NAME, database=DATABASE, user=USER, passwd=PASSWORD, use_pure=True)

# query = pd.read_sql('SELECT * FROM mytable;' , mydb)

# st.dataframe(query)

from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://root:Platinum79@127.0.0.1/pets'
db_connection = create_engine(db_connection_str)
st.write(db_connection)
# df = pd.read_sql('SELECT * FROM mytable', con=db_connection)

table_df = pd.read_sql_table(
    "mytable",
    con=db_connection
)
