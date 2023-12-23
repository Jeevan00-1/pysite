import requests
import streamlit as st
from streamlit_lottie import streamlit_lottie
import streamlit_lottie as st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":desktop_computer:U+1F5A5", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_event = "https://lottie.host/6c31cfb9-098f-4a8e-9083-627efea9f2ae/tIMEzkEDG2.json" 

with st.container():
    st.subheader("Hi, I am Jeevan Bastola :wave:")
    st.title("A programmer from Japan")
    st.write("I am currently working on a site for event planning and event participation.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.write(
            """
Discover Unforgettable Events in Ojima, Tokyo!

At JFF, we specialize in crafting extraordinary experiences that transcend expectations. Situated in the vibrant heart of Ojima, Tokyo, our seasoned team of event architects is dedicated to curating exceptional gatherings tailored to your desires.

Whether you're envisioning an intimate celebration, a corporate gala, a cultural festival, or a grand-scale event, we thrive on bringing your ideas to life with precision and flair. From meticulously chosen venues that showcase Ojima's unique charm to meticulously planned themes, exquisite décor, and seamless coordination, we handle every detail to ensure an unforgettable occasion.

Our commitment to excellence extends to a diverse range of events, including weddings, corporate conferences, product launches, and community festivals. With a keen understanding of local culture and a global perspective, we infuse each event with a touch of sophistication and cultural richness that epitomizes the spirit of Ojima.

Partner with us to transform your vision into an immersive reality. Let's collaborate to create moments that linger in memory long after the final toast.

Contact us today to embark on a journey to unparalleled events in Ojima, Tokyo!
"""
        )
    with right_column:
        st_lottie(lottie_event, height = 600, key ="coding")
