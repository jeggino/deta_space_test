import streamlit as st  

from deta import Deta
import pandas as pd



# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Create a new database
db = deta.Base("df")

st.dataframe(db)
