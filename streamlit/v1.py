import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = 'Tempus')
st.header("Tempus Dashboard")

#Read data
csv_file = 'save_csv.csv'
df = pd.read_csv(csv_file)
df2 = pd.read_csv('patient_result.csv')

ages = df2['Age'].unique().tolist()
drugs = df2['drugClass'].unique().tolist()

age_selection = st.slider('Age:', min_value = min(ages), max_value = max(ages), value=(min(ages), max(ages)))
drug_selection = st.multiselect('Drug:', drugs)


filter = (df2['Age'].between(*age_selection)) & (df2['drugClass'].isin(drug_selection))
num_cases = df2[filter].shape[0]
st.markdown(f'Result:{num_cases}')

df_filter = df2[filter]

st.dataframe(df_filter)

pie_chart = px.pie(title = 'Tissue', values = df_filter['tissue'].value_counts(), names = df_filter['tissue'].value_counts().index)
st.plotly_chart(pie_chart)


