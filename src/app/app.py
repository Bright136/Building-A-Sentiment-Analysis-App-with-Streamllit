import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from utils import run_sentiment_analysis, preprocess
from transformers import AutoTokenizer, AutoConfig,AutoModelForSequenceClassification
import os
import time

# the two model trained
dstbt_model_path = "bright1/fine-tuned-distilbert-base-uncased" # distilbert model
rbta_model_path = "bright1/fine-tuned-twitter-Roberta-base-sentiment" # roberta model

# function to load model 
def load_model_components(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    config = AutoConfig.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return model, tokenizer, config

# configure page
st.set_page_config(
    page_title="Tweet Analyzer",
    page_icon="🤖",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a Sentiment Analysis App. Call it the Covid Vaccine tweet Analyzer!"
    }
)  

# Define custom CSS style

# Apply custom CSS
# st.markdown("""<style> 
#         [data-testid="stAppViewContainer"] {
#             background-image: url("app\download.png");
#              background-attachment: fixed;
#             background-size: cover
#             }
# </style>""", unsafe_allow_html=True)



# create a sidebar and contents
st.sidebar.markdown("""
## Demo App

This app analyzes your tweets on covid vaccines and classifies them us Neutral, Negative or Positive
""")

# create a three column layout
model_type = st.sidebar.selectbox(label=':red[Select your model]', options=('distilbert', 'roberta'))
st.markdown("""<style> 
        [data-testid="stMarkdownContainer"] {
            font-size: 30px;
            font-weight: 800;
            }
</style>""", unsafe_allow_html=True)

# set a default model path
model_path = dstbt_model_path
if model_type == 'roberta':
    model_path = rbta_model_path


# create app interface 
my_expander  = st.container()

# st.sidebar.selectbox('Menu', ['About', 'Model'])
with my_expander:
    # center text in the container
    st.markdown("""
        <style>
        h1 {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)
    
    #set title for the app
    st.title(':green[Covid-19 Vaccines Tweets Analyzer]')


    # load model components
    model, tokenizer, config = load_model_components(model_path)


    # size columns
    col1, col2, col3 = st.columns((1.6, 1,0.3))
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
    
    # set textarea to receive tweet
    tweet = col1.text_area('Tweets to analyze',height=200, max_chars=520, placeholder='Write your Tweets here')

    # divide container into columns
    colA, colb, colc, cold = st.columns(4)
    clear_button = colA.button(label='Clear', type='secondary', use_container_width=True)

    # create a submit button
    submit_button = colb.button(label='Submit', type='primary', use_container_width=True)

    # set an empty container for the results
    empty_container = col2.container() # for progress bars
    empty_container.text("Results from Analyzer")

    empty_container2 = col3.container() # for scores
    empty_container2.text('Scores')
    text = preprocess(tweet)

    # run the analysis on the tweet
    results = run_sentiment_analysis(text=text, model=model, tokenizer=tokenizer)
    
    # when the tweet is submitted
    if submit_button:
        # print a success message 
        success_message = st.success('Success', icon="✅")
        time.sleep(3)
        success_message.empty()
        
        # create am expander to contain the results
        with empty_container:
            global neutral, negative, positive, neutral_score, positive_score, negative_score
            neutral = st.progress(value=results['Neutral'], text='Neutral')
            negative = st.progress(value=results['Negative'], text='Negative')
            positive = st.progress(value=results['Positive'], text='Positive')

        with empty_container2:
            st.markdown(
                """
            <style>
            [data-testid="stMetricValue"] {
                font-size: 20px;
            }
            .st-ed {
                background-color: #FF4B4B;  
            
            }
            .st-ee {
                background-color: #1B9C85;
            }
            .st-eb {
                background-color: #FFD95A;
            }
            </style>
            """,
                unsafe_allow_html=True,
            )

            # class=""
            # dispay the scores with metric widget 
            neutral_score = st.metric(label='Score', value=round(results['Neutral'], 4), label_visibility='collapsed')
            negative_score = st.metric(label='Score', value=round(results['Negative'], 4), label_visibility='collapsed')
            positive_score = st.metric(label='Score', value=round(results['Positive'], 4), label_visibility='collapsed')
            
            # interpret_button = col2.button(label='Interpret',type='secondary', use_container_width=True)
    if clear_button:
        tweet = ""



