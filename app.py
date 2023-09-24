from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 


st.set_page_config(page_title="My Page",page_icon=":kissing_face:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- Assets ---
coading = load_lottieurl("https://cdn.discordapp.com/attachments/703935965630169218/1155542317239914506/animation_lmxoak6l.json")
img_project = Image.open("images/1.png")

# --- Use Local CSS ---
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("style/style.css")


# ---- Header ----
with st.container():
    st.subheader("Hi I'm Sathira :wave:")
    st.title("A passionate IT Student form Sri Lanka 🇱🇰")
    st.write("Hello! I'm Sathira, a 20-year-old self-taught web developer 💻 and the founder 💼 of Enforcers.lk. I'm all about Python and web development 🌱 and currently exploring game dev, Node.js, and Java 🚀. Stay tuned for more tech adventures from me! 🌟💻🎮")
    st.write("[Github >](https://sathirasrisathsara.github.io)")

# --- What I do ----

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                - 🔭 I’m currently working on Enforcers.lk
                - 🌱 I’m currently learning Java.
                - I develop websites
                - I develop webapps
                - I develop programmes
                - somthig here
                - somthig here
                - somthig here
                - 📫 How to reach me sathira@enforcers.lk
            """
        )
    with right_column:
        st_lottie(coading, height=400, key="coding")


# --- Projects ---

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project)
    with text_column:
        st.subheader("The Projects Thas I have been Working On..")
        st.write(
            """
                This is description about project
            """
        )


# --- Contact Form ---

contact = """
<form id="contactform" action="https://formsubmit.io/send/sathira@enforcers.lk" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input name="name" type="text" placeholder="Your name" id="name" required>
    <input name="email" type="email" placeholder="Your email" id="email" required>
    <textarea name="message" id="comment" rows="3" placehoader="Your message here" required></textarea>
    <input name="_formsubmit_id" type="text" style="display:none">
    <button value="Submit" type="submit">Submit</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact, unsafe_allow_html=True)
with right_column:
    st.empty()