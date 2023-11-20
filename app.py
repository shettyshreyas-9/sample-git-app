import streamlit as st


st.title('Sukuna')

col1, col2= st.columns(2)

with col1:
    st.image('sukuna_7.jpg')

with col2:
    st.write("""
                "Sukuna" refers to Ryomen Sukuna, a fictional character in the Japanese manga and anime series "Jujutsu Kaisen." "Jujutsu Kaisen" is written and illustrated by Gege Akutami. The series follows the story of Yuji Itadori, a high school student with exceptional physical abilities. After encountering a cursed object and dark sorcery, Yuji becomes involved in the world of curses and jujutsu sorcery.

Ryomen Sukuna is a powerful and malevolent Cursed Spirit, known as a legendary and fearsome figure in the series. He was a human sorcerer from the past who became the King of Curses after his death. Sukuna is infamous for his strength and cruelty, and he is considered one of the most dangerous Cursed Spirits in the Jujutsu Kaisen universe.

In the series, Sukuna's curse is contained within a collection of cursed fingers, and the story revolves around the efforts of jujutsu sorcerers, including Yuji Itadori, to collect and deal with these cursed objects. Sukuna's presence poses a significant threat, and his influence on the events in the series is profound.

"Sukuna" is a central element in the narrative, contributing to the dark and action-packed atmosphere of "Jujutsu Kaisen." The character's design and abilities have made him a notable and memorable part of the series for fans of the manga and anime.
             """)

st.header('"Sukuna" refers to Ryomen Sukuna...!')
st.subheader('- Ryomen Sukuna is a powerful and malevolent Cursed Spirit')
st.subheader('- King of Curses')
st.subheader("- Sukuna's fingers")

st.header("Sukuna's quotes")
st.subheader("- Know your place")
st.subheader("- What a waste of talent...")


st.sidebar.title('Powers')
st.sidebar.markdown('''
- Domain Expansion: Malevolent Shrine
- Curse Manipulation
- Super Strength
''')


st.sidebar.selectbox('Game Type',["story mode","one on one battle"])
st.sidebar.button('Start')

st.title('The Story mode begins...!')