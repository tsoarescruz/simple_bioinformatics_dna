####################
# Import libraries
####################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

####################
# Page Title
####################

# image = Image.open('./img/dna-logo.jpeg')
# st.image(image, use_collumn_width=true)

st.write("""
# DNA Nucleotide Count Web app

This app counts the nucleotide composition of query DNA!
***
""")

####################
# Import Text Box
####################


st.header('Enter DNA Sequence')

sequence_input = "> DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
# sequence = sequence.splitelines() + sequence[1:]
sequence = sequence.splitlines()
sequence = sequence[1:]

sequence = ''.join(sequence)

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Nucleotide Count)')
sequence


## DNA Nucleotide Count
st.header('OUTPUT (DNA Nucleotide Count)')


### 1 - Print dictionary

st.subheader('1 - Print Dictionary')

def dna_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = dna_nucleotide_count(sequence)

X

### 2 - Print Text

st.subheader('3. Display DataFrame')

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotides'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotides',
    y='count'
)
p = p.properties(
    width=alt.Step(60)  # controls width of bar.
)
st.write(p)