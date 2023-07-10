from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from textblob import TextBlob

# Enhancement functions
def enhance_title(title):
    return title + " - The Best on the Market!"

def enhance_desc(desc):
    return "This product will make you happier and more productive. " + desc 
        
def main():
    st.title("Rosemary: product properties enhancement and marketing auxiliary")
    st.write("Turn your product words into sales!") 

    # Input fields
    original_title = st.text_input("Original Title")
    original_desc = st.text_area("Original Description")
    
    # Button to trigger execution
    if st.button("Enhance My Product Properties!"):    
        # Enhance text  
        enhanced_title = enhance_title(original_title)
        enhanced_desc = enhance_desc(original_desc)
        
        
        # Display results
        st.subheader("Original")
        st.write("Title: ", original_title)
        st.write("Description: ", original_desc)
        
        st.subheader("Enhanced")
        st.write("Title: ", enhanced_title)  
        st.write("Description: ", enhanced_desc)

        
if __name__ == '__main__':
    main()
