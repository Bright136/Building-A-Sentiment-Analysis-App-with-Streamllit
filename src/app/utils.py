import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoConfig,AutoModelForSequenceClassification
from scipy.special import softmax
import os



def check_csv(csv_file, data):
    if os.path.isfile(csv_file):
        data.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8')
    else:
        history = data.copy()
        history.to_csv(csv_file, index=False)

#Preprocess text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = "@user" if t.startswith("@") and len(t) > 1 else t
        t = "http" if t.startswith("http") else t
        print(t)
        new_text.append(t)

    return " ".join(new_text)

#Process the input and return prediction
def run_sentiment_analysis(text, tokenizer, model):
    # save_text =  {'tweet': text}
    encoded_input = tokenizer(text, return_tensors = "pt") # for PyTorch-based models
    output = model(**encoded_input)
    scores_ = output[0][0].detach().numpy()
    scores_ = softmax(scores_)

    # Format output dict of scores
    labels = ["Negative", "Neutral", "Positive"]
    scores = {l:float(s) for (l,s) in zip(labels, scores_) }
    # save_text.update(scores)
    # user_data = {key: [value] for key,value in save_text.items()}
    # data = pd.DataFrame(user_data,)
    # check_csv('history.csv', data)
    # hist_df = pd.read_csv('history.csv')
    return scores


    

