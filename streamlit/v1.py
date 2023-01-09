import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = 'Tempus')
st.header("Tempus Dashboard")

#Read data

df2 = pd.read_csv('patient_result.csv')
ages = df2['Age'].unique().tolist()
# drugs = df2['drugClass'].unique().tolist()
filters = ['therapy', 'drugClass', 'tissue', 'variant', 'evidenceType', 'association', 'status', 'url', 'pubMedId', 'fdaApproved', 'isOnLabel']
for i in filters:
    globals()[f'{i}'] = df2[i].unique().tolist()



select_filters = st.multiselect(f'', filters)
my_slot2 = st.empty()

#select_filters = ['therapy']

age_selection = st.slider('Age:', min_value = min(ages), max_value = max(ages), value=(min(ages), max(ages)))
filter = (df2['Age'].between(*age_selection)) 
# num_cases = df2[filter].shape[0]
# st.markdown(f'Result:{num_cases}')
# drug_selection = st.multiselect('Drug:', drugs)
for i in select_filters:
    globals()[f'{i}_selection'] = st.multiselect(f'{i}:', globals()[f'{i}'])
    if len(globals()[f'{i}_selection']) != 0:
        filter = filter & (df2[i].isin(globals()[f'{i}_selection']))
    num_cases = len(df2[filter]['filename'].unique().tolist())
    st.markdown(f'Result:{num_cases}')
    my_slot2.markdown(f'Result:{num_cases}')



num_cases = df2[filter].shape[0]




# filter = (df2['Age'].between(*age_selection)) & (df2['drugClass'].isin(drugClass_selection))
df_filter = df2[filter]

st.dataframe(df_filter)

pie_chart = px.pie(title = 'Tissue', values = df_filter['tissue'].value_counts(), names = df_filter['tissue'].value_counts().index)
st.plotly_chart(pie_chart)


