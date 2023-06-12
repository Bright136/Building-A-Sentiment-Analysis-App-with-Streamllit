# Building A Sentiment Analysis App with Streamlit

<div align='center'> 
    <img src="https://drive.google.com/uc?export=view&id=1EAyNzwMOaJPJrDUFHkz6tyqfLJokkWoS"/>

</div>
This is a streamlit app that performs sentiment analysis on COVID-19 tweets using two pre-trained language models, DistilBERT and RoBERTa.

## Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| LP5 | Sentiment Analysis App with Stramlit |  [Deploying an App on Hugging Face](https://medium.com/@brighteshun/deploying-a-sentiement-analysis-app-on-huggingface-faeb43954905) | [Streanlit App](https://huggingface.co/spaces/bright1/sentiment-analysis-app-streamlit) |

			
## Project Description
The aim of this project is to analyze the sentiment of tweets related to COVID-19 using two pre-trained language models, DistilBERT and RoBERTa. The app takes in user-generated text input and predicts whether the sentiment of the tweet is Negative, Neutral, or Positive. The app also preprocesses the input text by replacing any mention of usernames with "@user" and replacing any URLs with "http".

How the app works

- Select the model type from the dropdown list. You can choose between DistilBERT and RoBERTa.
- Type your tweet or text in the text area provided.
- Click on the "Analyze" button to get the sentiment analysis of your input text.

## Setup
To set up the project locally, follow these steps:

- Clone the repository using:
        
        git clone https://github.com/Bright136/Building-A-Sentiment-Analysis-App-with-Streamllit.git

OR

You can download the code 

At the root repository 

`root :: Building-A-Sentiment-Analysis-App-with-Streamllit> ...`

Do:
- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv ve  nv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt


## App Execution
To execute the app, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
run the command: 
            gradio .\scr\app\app.py

Open your browser and go to http://localhost:8501/

## Screenshots

<span>Photos of the Gradio App</span>

<div align='center'> 
    <img src="https://drive.google.com/uc?export=view&id=1EAyNzwMOaJPJrDUFHkz6tyqfLJokkWoS"/>

</div>

## Author

<table>
  <tr>
    <th>Name</th>
    <th>Twitter</th>
    <th>LinkedIn</th>
    <th>GitHub</th>
    <th>Hugging Face</th>
  </tr>
  <tr>
    <td>Bright Eshun</td>
    <td><a href="https://twitter.com/bright_eshun_">@bright_eshun_</a></td>
    <td><a href="https://www.linkedin.com/in/bright-eshun-9a8a51100/">@brighteshun</a></td>
    <td><a href="https://github.com/Bright136">@bright136</a></td>
    <td><a href="https://huggingface.co/bright1">@bright1</a></td>
  </tr>
</table>