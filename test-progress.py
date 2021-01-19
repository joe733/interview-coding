import streamlit as slt
import time

latest_iteration = slt.empty()
bar = slt.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

'... and now we\'re done!'
