# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 02:45:11 2023

@author: tosha
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

file = r'C:\Users\tosha\Downloads/Billionaire.csv'
st.header ('Billionaire Dataset')

# reading the file
df = pd.read_csv(file)


#for excel files type following codes
#df = read_excel(file name)
#names =  df.sheet_names
#all_data = []
#for name in names:
 #       all_data.append(df[name])


#df = st.file_uploader(label= 'upload your file', type= 'csv')
#button = st.button ('upload')

#data cleaning
df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace('B', '')))


#interactivity
#all_countries = df['Country'].unique()
#selection = st.selectbox('select Country', all_countries)
#subset = df[df['Country'] == selection]
#st.dataframe(subset)


#containers
all_countries = sorted(df['Country'].unique())
col1,col2 = st.columns(2)
#column 1

#display on streamlit
selected_country = col1.selectbox('Select you Country', all_countries)
#subset on selected country
subset_country = df[df['Country'] == selected_country]
#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
#display multi select option on source
selected_source = col1.multiselect('select source o f income', sources)
#subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

#column 2
 
main_string ='{} - Billionaires'.format(selected_country)
#main_string = selected_country +' - Billionaires'
col2.header(main_string)
col2.dataframe(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)


#find count of billionaires by country:
#bill_count = df.groupby('Country')['Name'].count().sort_values(ascending=False).head(10)


st.dataframe(bill_count)
#st.bar_chart(bill_count)
#st.pyplot()
# find the most popular source of income

# get the cumulative wealth of billionaires belonging to US