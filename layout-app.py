from typing import Optional
import streamlit as slt
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# st.sidebar.[element_name]()
# st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart()

option = slt.sidebar.selectbox(
    'Which number do you prefer?',
    df['first column']
)

'Your selection: ', option

left_column, right_column = slt.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = slt.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
