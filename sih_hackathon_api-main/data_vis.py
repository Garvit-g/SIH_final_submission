import streamlit as st
import pandas as pd

df = pd.DataFrame(columns=["x", "y"])

with st.form("insertion_form"):
    st.write("Add data")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# st.subheader("Add Record")

# num_new_rows = st.sidebar.number_input("Add Rows",1,50)
# ncol = df.shape[1]  # col count
# rw = -1

# with st.form(key="add form", clear_on_submit= True):
    # cols = st.columns(ncol)
    # rwdta = []

    # for i in range(ncol):
    #     rwdta.append(cols[i].text_input(st.session_state.df.columns[i]))

    # # you can insert code for a list comprehension here to change the data (rwdta) 
    # # values into integer / float, if required

    # if st.form_submit_button("Add"):
    #     if df.shape[0] == num_new_rows:
    #         st.error("Add row limit reached. Cant add any more records..")
    #     else:
    #         rw = df.shape[0] + 1
    #         st.info(f"Row: {rw} / {num_new_rows} added")
    #         df.loc[rw] = rwdta

    #         if df.shape[0] == num_new_rows:
    #             st.error("Add row limit reached...")

st.dataframe(df)