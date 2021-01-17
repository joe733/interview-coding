# streamlit run [filename]
import streamlit as slt
import pandas as pd

df = pd.DataFrame(
    {'First Column' : [1, 'abc', '12'],
    'Second Column' : [21, '', [4, 2]]}
)

df