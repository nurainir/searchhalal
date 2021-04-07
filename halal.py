import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re
import string
import requests
from sklearn.feature_extraction.text import TfidfVectorizer


# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'



st.title("Assalamu 'alaikum ")

cari = st.text_input("Cari Produk/Restaurant Halal", "soto ")
  
# display the name when the submit button is clicked
# .title() is used to get the input text string 
if(st.button('Submit')):
    result = cari.title()
    if(result):
    	st.success(result)
    else:
    	st.error("Masukkan input ya")




df = pd.DataFrame(
    np.random.randn(5, 4),
    columns=('col %d' % i for i in range(4))
)
st.image("produk.png", width=None)

st.write("Top 5 Halal")
st.table(df.style.set_precision(2))

st.header("WordCloud Nama Produk tersertifikasi Halal di LPPOM MUI")

wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot(plt)

st.header("WordCloud Nama Perusahaan tersertifikasi Halal di LPPOM MUI")

st.markdown("---")
st.markdown("**Awards**")
st.markdown("- Best Graphistry app at Tigergraph Hackathon 2021")
st.markdown("- Neo4J Graphie Winner 2020")
st.markdown("- Best Paper at International Conference on Halal Innovation in Products and Services 2018")


st.header("Pusat Kajian Halal ITS")
