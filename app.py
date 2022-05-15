#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:14:39 2022

@author: lilitharutyunyan
"""

import streamlit as st

st.title("Real-Time / Live Country Dashboard")

st.write("""
        # Exploring countries based on their population, life expectancy and GNI per capita
        """)
        

import pandas as pd             


data = pd.read_csv("/Users/lilitharutyunyan/Desktop/streamlit.csv") #path folder of the data file
st.write(data) #displays the table of data



st.subheader("Year Slider")
x = st.slider('data["year"]')

st.write("Slider number:", x)

options = st.multiselect(
     'Select country',
     data["country"])

st.write('You selected:', options)

import numpy as np
sidebars = {}
for y in data.columns:
    if (data[y].dtype == np.object):
        columns=list(data[y].unique())
        sidebars[y+"filter"]=st.sidebar.multiselect('Filter '+y, columns)