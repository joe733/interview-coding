import streamlit as slt
import numpy as np
import pandas as pd

slt.title("Test streamlit data")
slt.write('''
## This is the second title

> This happens to be quote

- This is a bulltedted list
- Second item of list

This is crazy!
''')

# Let's use this swiss army knife!
slt.write("Let's write some table: ")
slt.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, '3', 'Jac', (1, 4)]
}))

