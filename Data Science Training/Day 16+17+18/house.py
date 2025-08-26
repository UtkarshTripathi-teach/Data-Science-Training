import streamlit as st
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
import pickle


# Title

col = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']

st.title('California Housing Price Prediction')
st.image('https://media.istockphoto.com/id/1192403701/photo/residential-housing-background.jpg?s=612x612&w=0&k=20&c=8iquSynRiqeXDRaE53-0aKNEGe8y7RKslG2SoYwYGAQ=',width=680)


st.header('A model of housing prices to predict median house values in California',divider=True)
# st.subheader(''' User must enter given values to predict price:
# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']''')


st.sidebar.header("Select House Features 🏠")

st.sidebar.image('https://img.freepik.com/premium-photo/stylized-blue-white-houses-arranged-row-blue-gradient-background_276930-6237.jpg')



# read_data

temp_df = pd.read_csv('california.csv')

random.seed(20)

all_values = []

for i in temp_df[col]:
    min_value, max_value = temp_df[i].agg(['min','max'])

    var = st.sidebar.slider(f'Select{i} range',int(min_value),int(max_value),random.randint(int(min_value),int(max_value)))

    all_values.append(var)


ss = StandardScaler()
ss.fit(temp_df[col])

final_value = ss.transform([all_values])


with open('house_price_pred_ridge_model.pkl','rb') as f:
    chatgpt = pickle.load(f)

price = chatgpt.predict(final_value)[0]

import time


st.write(pd.DataFrame(dict(zip(col,all_values)),index = [1]))


value = 0
progress_bar = st.progress(0)
placeholder = st.empty()
placeholder.subheader('Predicting Price!!')
place = st.empty()
place.image('https://scitechdaily.com/images/Radar-Concept.gif',width=190)



if price>0:

    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i+1)
        

    body = f'**Predicted Median House Price:${round(price,2)}Thousand Dollars**'
    # st.subheader(body)
    st.success(body)
    placeholder.empty()
    place.empty()
else:
    body = 'Invalid House features Value'
    st.warning(body)







st.markdown("""
    <hr style="margin-top: 50px;">
    <div style="text-align: center; color: gray;">
        <small>Utkarsh Tripathi &copy</small>
    </div>
""", unsafe_allow_html=True)
