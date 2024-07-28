# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

import streamlit as st

# Title
st.title('Hello, Streamlit!')

# Header
st.header('This is a header')

# Subheader
st.subheader('This is a subheader')

# Text
st.text('Hello, this is some text.')

# Markdown
st.markdown('### This is a markdown text')

# Input fields
name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')

number = st.number_input('Enter a number:')
st.write(f'The number you entered is: {number}')

# Button
if st.button('Click me'):
    st.write('Button clicked!')

# Selectbox
option = st.selectbox(
    'Choose an option:',
    ['Option 1', 'Option 2', 'Option 3']
)
st.write(f'You selected: {option}')

