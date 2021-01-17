import streamlit as slt
import pandas as pd
import numpy as np

if slt.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    slt.line_chart(chart_data)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

option = slt.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option