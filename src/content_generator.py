import streamlit as st
import os
import cohere
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
co = cohere.Client(api_key)
st.title("Blog Content Generator")

use_case = "Blog"
if use_case=="Email":
    with st.form("my_form_2"):
        receipient = st.text_input("To Who?")
        subject = st.text_input("What is the subject of your email")
        bullets = st.text_area("What are the main points you want to make?",placeholder="Example: We have a meeting next week. \n I will be providing light refreshments")
        tone = st.selectbox("Tone", ("","Formal","Informal", "Frienldy","Caring"))
        creativity = st.slider(label="Creativity",min_value=0.0,max_value=3.0, value=1.0, step=.25)
        length = st.slider("Approximate Generation Length(words)", min_value=10, max_value=300, value=100)
        submitted = st.form_submit_button("Submit")
else:
    with st.form("my_form_3"):
        tone = st.selectbox("Tone(Optional)", ("Friendly","Casual", "Formal", "Persuasive", "Informative", "Funny", "Serious", "Clever", "Creative", "Boring"))
        creativity = st.slider(label="Creativity",min_value=0.0,max_value=3.0, value=1.0, step=.25)
        subject = st.text_area("What should I write about?")
        submitted = st.form_submit_button("Submit")

n_gens=1
freq=0.5
def generate(prompt,model_size="xlarge",n_generations=n_gens, temp=.75, tokens=250, stops=["--"], freq=freq):
    prediction = co.generate(
                    model=model_size,
                    prompt=prompt,
                    return_likelihoods = 'GENERATION',
                    stop_sequences=stops,
                    max_tokens=tokens,
                    temperature=temp,
                    num_generations=n_generations,
                    k=0,
                    frequency_penalty=freq,
                    p=0.75)
    return(prediction)

def max_likely(pred):
    print(pred)
    return pred.generations[0].text
    

with st.spinner('Generating Content...'):
    if submitted:
        if use_case == "Blog":
            
            prompt = "Write a blog about \n\n " + subject + "\n\n" +  "Write it in a " + tone + " tone."
            prediction = generate(prompt=prompt, model_size='command-xlarge-20221108', temp=creativity, tokens=500, stops=["----"])
            content = max_likely(prediction)
            prompt2 = "Write a creative title for this blog. \n\n" + "Blog:" + content + "\n\nTitle:"
            prediction = generate(prompt=prompt2, model_size='command-xlarge-20221108', temp=creativity, tokens=25, stops=["---"])
            title = max_likely(prediction)
            
            st.header(title)
            st.write(content)
        if use_case == "Email":
            
            prompt="Write an email to " + receipient + " about " + subject + "\n\n" + "Write it in a " + tone + " tone.\n\n" + "The main points are:\n\n" + bullets
            prediction = generate(prompt=prompt, model_size='command-xlarge-20221108', temp=creativity, tokens=length*3, stops=["----"])
            content = max_likely(prediction)
            st.balloons()
            st.write(content)
