#streamlit

import streamlit as st

st.set_page_config(page_title="growth minset project", project_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app will help you develop a growth mindset")

# quote section

st.header("💡 Today's Growth Minset Quote")
st.write("'To improve is to change; to be perfect is to change often' - Practice Continuous Improvement. 'Success is the ability to go from one failure to another with no loss of enthusiasm' - Maintain Your Passion.")

st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Describe a Chellenge you are facing:")

#condition
if user_input:
    st.success(f"🦦 You are facing: {user_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")
    
    
#reflexing
st.header("Reflection on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great insight! Your reflection: {reflection}")
    
else:
    st.info("Reflection on past experience help you grow! Share your deficulties")
    

#achivements
st.header("🏆 Celebrate Your Wins!")
achivements = st.text_input("Share something you've recently accomplished:")

if achivements:
    st.success(f"🎉 Amazing! You achived: {achivements}")
    
else:
    st.info("Big or small, every achivement counts! Share your win")
    
#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination!  ✨")
st.write("**© Created by Suleman Sehar**")
st.write("Find me on {https://www.linkedin.com/in/suleman-sehar-a60655106/}")
    