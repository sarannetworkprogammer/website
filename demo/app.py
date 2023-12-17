import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout= "wide")

#st.write("##")

#st.subheader("Hey Guys :wave: ")

#st.title("My Portfolio Website")





#st.write(""" I am going to build personal website to show case portfolio""")

#st.write("[Linkedin](https://www.linkedin.com/in/saran-m-6384a299/)")

#st.write('----')


with st.container():
    selected = option_menu(
        menu_title= None,
        options = ['About', 'Projects', 'Technical_skills', 'Experience', 'Contact', 'Resume','Certifications'],
        orientation= 'horizontal'
    )


if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.write("####")
            st.subheader("I am Saran")
            st.title("Masters at UTSA")