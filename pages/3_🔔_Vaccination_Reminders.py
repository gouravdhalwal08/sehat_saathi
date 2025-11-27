import streamlit as st
import database as db
from core.language import TEXT
import datetime
import pandas as pd

# Ensure language is set
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

T = TEXT[st.session_state.lang]

st.header(T["reminders_header"])
st.info(T["reminders_intro"])

# --- FORM TO ADD NEW REMINDER ---
with st.form("reminder_form", clear_on_submit=True):
    st.subheader(T["reminders_form_header"])
    child_name = st.text_input(T["reminders_child_name"])
    vaccine_name = st.text_input(T["reminders_vaccine_name"])
    due_date = st.date_input(T["reminders_due_date"], min_value=datetime.date.today())
    submitted = st.form_submit_button(T["reminders_add_button"])

    if submitted:
        if child_name and vaccine_name:
            db.add_reminder(child_name, vaccine_name, due_date)
            st.success(T["reminders_success"])
        else:
            st.error("Please fill in all the fields.")

st.markdown("---")

# --- DISPLAY AND MANAGE REMINDERS ---
st.subheader(T["reminders_table_header"])

reminders_df = db.get_reminders_as_df()

if reminders_df.empty:
    st.write(T["reminders_empty"])
else:
    # Make the DataFrame editable
    reminders_df['due_date'] = pd.to_datetime(reminders_df['due_date']).dt.date
    
    edited_df = st.data_editor(
        reminders_df,
        column_config={
            "status": st.column_config.SelectboxColumn(
                "Status",
                options=["Pending", "Done"],
                required=True,
            ),
            "id": None # Hide the ID column
        },
        hide_index=True,
        num_rows="dynamic", # Allow deleting rows
        key="reminder_editor"
    )

    # Check if the DataFrame has been changed by the user
    if not edited_df.equals(reminders_df):
        db.update_reminder(edited_df)
        st.toast("Changes saved!")
        st.experimental_rerun() # Use experimental_rerun for older versions if rerun fails