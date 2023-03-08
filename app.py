# streamlit_app.py

import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://root:Platinum79@127.0.0.1/ebird'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM obs_df', con=db_connection)

st.dataframe(df)
