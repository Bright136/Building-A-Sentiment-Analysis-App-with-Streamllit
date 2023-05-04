import streamlit as st
import pandas as pd
import numpy as np
# from scipy.special import softmax
# import os
from utils import run_sentiment_analysis



# dark_theme = set_theme()


st.set_page_config(
    page_title="Tweet Analyzer",
    page_icon="🤖",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)  


my_expander  = st.container()

# st.sidebar.selectbox('Menu', ['About', 'Model'])
with my_expander:
    st.markdown("""
        <style>
        h1 {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)
    st.title(':green[Covid-19 Tweets Analyzer]')
    st.sidebar.markdown("""
    ## Demo App

    This app analyzes your tweets and classifies them us Neutral and Negative, Positive
    """)        
    
    # create a three column layout

    col1, col2 = st.columns(2)
    # col2.markdown("""
    #         <p style= font-color:red>
    #             Results from Analyzer
    #         </p>
    # """,unsafe_allow_html=True)
    st.markdown("""
        <style>
        p {
            font-color: blue;
        }
        </style>
        """, unsafe_allow_html=True)
    tweet = col1.text_area('Tweets to analyze',height=200, max_chars=520, placeholder='Write your Tweets here')
    colA, colb, colc, cold = st.columns(4)
    clear_button = colA.button(label='Clear', type='secondary', use_container_width=True)
    submit_button = colb.button(label='Submit', type='primary', use_container_width=True)
    interpret_button = cold.button(label='Interpret',type='secondary', use_container_width=True)
    emnpty_expander = col2.empty()
    if submit_button:
        st.success('Success', icon="✅")
        print(run_sentiment_analysis(tweet))
        with emnpty_expander.expander(label='Results from Analyzer',expanded=True):
            neutral = col2.progress(value=0.24, text='neutral', )
            negative = col2.progress(value=0.56, text='negative')
            positive = col2.progress(value=0.38, text='positive')


# st.help()
    # create a date input to receive date

