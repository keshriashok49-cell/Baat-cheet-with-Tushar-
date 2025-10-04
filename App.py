import streamlit as st
import random
import csv

# Funny reply function
def funny_reply(category):
    replies = {
        "greeting": ["Heyy superstar!", "Yo! Tushar aa gaya", "Hello hello, legend incoming"],
        "flirt": ["Hmmm interesting", "Ohho, kuch toh special hai", "Waah waah, waise tumhare jaise log rare h"],
        "funny": ["Hahaha sahi bola", "Lol! Tum toh comedian ho", "Seriously, maza aa gaya sun ke!"]
    }
    return random.choice(replies.get(category, ["Nice!"]))

st.title("Tushar ka Fun Chat 😗")
st.write("Aaj tumhare saath chat karne ka mood hai 😗")

answers = {}

# Input fields
answers["name"] = st.text_input("Enter your name:")
answers["age"] = st.number_input("What's your age:", min_value=0, max_value=120, step=1)
answers["field"] = st.text_input("Which field are you interested in?")
answers["language"] = st.radio("Mai Hindi mai baat kar sakta hu?", ["yes", "no"])
answers["first_meeting"] = st.selectbox("First time mile the?", ["school", "instagram", "coaching"])
answers["favorite_game"] = st.text_input("Kaunsa game pasand hai?")
answers["favorite_food"] = st.text_input("Kya khana pasand hai?")
answers["future_plan"] = st.text_input("Tushar ke saath future me kahan ghumna chahoge?")
answers["tushar_physical"] = st.radio("Tushar aapko physically kaisa lagta hai?", ["handsome", "normal", "funny"])
answers["tushar_dressing"] = st.radio("Tushar ka dressing style kaisa lagta hai?", ["cool", "casual", "simple"])
answers["tushar_talking"] = st.radio("Tushar ka baat karne ka tarika kaisa lagta hai?", ["friendly", "rude", "funny"])

# Submit button
if st.button("Submit"):
    # Save responses to CSV
    with open("responses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(list(answers.values()))
    
    st.success("Thanks for sharing! Your answers are saved 😗")
    
    # Fun replies on web page
    st.write(f"Hello {answers['name']}! {funny_reply('greeting')}")
    st.write(f"Wow great! Your age is {answers['age']} {funny_reply('flirt')}")
    if answers['age'] >= 18:
        st.write("Now you are eligible for: vote, driving, aur aur bhi bohot saari masti")
        if answers['age'] >= 90:
            st.write("So sad... ab tak zinda ho, dharti pe bojh!")
    else:
        st.write("Koi nahi bhai, 18 ke baad life ka full fun milega")
    
    st.write(f"{answers['field']}? Wah, Tushar bhi is field ke fan hai")
    if answers['language'] == "yes":
        st.write(f"Haa, Hindi mai baat karna best hai {funny_reply('flirt')}")
    else:
        st.write("English bhi chalega, par thoda funny ho jayega")
    st.write(f"Ah yes, {answers['first_meeting']} memories are unforgettable! {funny_reply('funny')}")
    st.write(f"{answers['favorite_game']}? Nice choice! {funny_reply('flirt')}")
    st.write(f"{answers['favorite_food']}? Sounds yummy {funny_reply('funny')}")
    st.write(f"Wah! {answers['future_plan']} me ghumna maza ayega! {funny_reply('flirt')}")
    st.write(f"Tushar aapko {answers['tushar_physical']} lagta hai {funny_reply('flirt')}")
    st.write(f"{answers['tushar_dressing']} style? Perfect! {funny_reply('funny')}")
    st.write(f"{answers['tushar_talking']}? Got it! {funny_reply('flirt')}")
    st.balloons()
