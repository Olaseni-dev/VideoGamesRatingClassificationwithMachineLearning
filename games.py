import streamlit as st
import pandas as pd
from joblib import load
import numpy as np
from sklearn.pipeline import make_pipeline

# Load the saved model
with open('model_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

# Title of the application
st.title('Video Games Ratings')

# Dropdown for Year of Release
year_of_release = st.selectbox(
    'Year of Release',
    list(range(2000, 2017))
)

# Dropdown for Genre
genre = st.selectbox(
    'Genre',
    ['Sports', 'Racing', 'Platform', 'Misc', 'Action', 'Puzzle',
     'Shooter', 'Fighting', 'Simulation', 'Role-Playing', 'Adventure',
     'Strategy']
)

# Dropdown for Platform
platform = st.selectbox(
    'Platform',
    ['Wii', 'DS', 'X360', 'PS3', 'PS2', 'Average', 'XB', 'PC', 'Unpopular']
)

# Dropdown for Publisher
publisher = st.selectbox(
    'Publisher',
    ['Nintendo', 'Microsoft Game Studios', 'Take-Two Interactive',
     'Sony Computer Entertainment', 'Activision', 'Ubisoft',
     'Bethesda Softworks', 'Electronic Arts', '505 Games',
     'Konami Digital Entertainment', 'Square Enix',
     'Sony Computer Entertainment Europe', 'LucasArts', 'Capcom',
     'Warner Bros. Interactive Entertainment', 'Universal Interactive',
     'Unpopular', 'Average', 'Atari', 'Namco Bandai Games',
     'Eidos Interactive', 'MTV Games', 'Disney Interactive Studios',
     'Sega', 'THQ', 'Majesco Entertainment', 'Virgin Interactive',
     'Acclaim Entertainment', 'Midway Games', 'Deep Silver',
     'Vivendi Games', 'NCSoft', 'Tecmo Koei', 'Infogrames', 'Mindscape',
     'Activision Value', 'Global Star', 'Crave Entertainment',
     'Rising Star Games', 'Codemasters', 'TDK Mediactive', 'Zoo Games',
     'Sony Online Entertainment', 'RTL', 'D3Publisher',
     'SouthPeak Games', 'Zoo Digital Publishing', 'City Interactive',
     'Empire Interactive', 'Atlus', 'Mastertronic', 'Play It', 'GSP',
     'Tomy Corporation', 'Focus Home Interactive', 'Koch Media',
     'Unknown', 'Game Factory', 'Titus', 'SCi', 'Ubisoft Annecy',
     'Scholastic Inc.', 'Hudson Soft', 'Nobilis', 'Spike',
     'Nippon Ichi Software', 'Interplay', 'Metro 3D', 'Rondomedia',
     'Ghostlight', 'PQube', 'Ignition Entertainment', 'Natsume', '3DO',
     'Destineer', 'Midas Interactive Entertainment', 'XS Games',
     'Xplosiv', 'System 3 Arcade Software', 'BAM! Entertainment',
     'GameMill Entertainment', 'Mastiff', 'Telegames', 'GungHo',
     'Avanquest', 'Black Bean Games', 'Takara Tomy', 'Zushi Games',
     'Sammy Corporation', 'Brash Entertainment', 'Oxygen Interactive',
     'PopCap Games', 'Gathering of Developers', 'Marvelous Interactive',
     'Kalypso Media', 'Arc System Works', 'Storm City Games',
     'Nordic Games', 'Mumbo Jumbo', 'Little Orbit', 'DTP Entertainment',
     'Kemco', 'Milestone S.r.l.', 'Telltale Games', 'Aspyr',
     'Compile Heart', 'JoWood Productions', 'UFO Interactive', 'Jaleco',
     'Playlogic Game Factory', 'Paradox Interactive',
     'DreamCatcher Interactive', 'Sting', 'Idea Factory',
     'Destination Software, Inc', 'Graffiti', 'From Software',
     'Bigben Interactive', 'O-Games', 'Valcon Games', 'Microids',
     'Conspiracy Entertainment', 'Evolved Games', 'Popcorn Arcade',
     'Aksys Games', 'Success']
)

# Int TextBox for Global Sales
global_sales = st.number_input('Global Sales', min_value=1)

# Int TextBox for Critic Score
critic_score = st.number_input('Critic Score', min_value=1, max_value=100)

# Int TextBox for Critic Count
critic_count = st.number_input('Critic Count', min_value=1)

# Int TextBox for User Score
user_score = st.number_input('User Score', min_value=1, max_value=10)

# Int TextBox for User Count
user_count = st.number_input('User Count', min_value=1)

# Perform additional calculations based on user input
average_score = critic_score + user_score
score_difference = critic_score - user_score
total_reviews = critic_count + user_count
sales_per_review = global_sales / total_reviews
critic_engagement = critic_count / critic_score


# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Year_of_Release': [year_of_release],
    'Genre': [genre],
    'Platform': [platform],
    'Publisher': [publisher],
    'Global_Sales': [global_sales],
    'Critic_Score': [critic_score],
    'Critic_Count': [critic_count],
    'User_Score': [user_score],
    'User_Count': [user_count],
    'Average_Score': [average_score],
    'Score_Difference': [score_difference],
    'Total_Reviews': [total_reviews],
    'Sales_per_Review': [sales_per_review],
    'Critic_Engagement': [critic_engagement]
})

# Make prediction
if st.button('Predict'):
    prediction = model_pipeline.predict(input_data)
      # Customize the result
    if prediction[0] == 0:
        st.write('Predicted Rating:', 'E (Everyone)')
    elif prediction[0] == 1:
        st.write('Predicted Rating:', 'T (Teen)')
    elif prediction[0] == 2:
        st.write('Predicted Rating:', 'M (Mature)')
    elif prediction[0] == 3:
        st.write('Predicted Rating:', 'E10+ (Everyone 10 and older)')