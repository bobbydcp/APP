import streamlit as st
import pandas as pd
import os

def main():
    st.set_page_config(page_title="User Form", page_icon="📝", layout="centered")
    st.title("User Information Form")
    
    file_path = "user_data.xlsx"
    
    with st.form(key="user_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            new_data = pd.DataFrame({"Name": [name], "Email": [email], "Phone": [phone], "Message": [message]})
            
            if os.path.exists(file_path):
                existing_data = pd.read_excel(file_path)
                updated_data = pd.concat([existing_data, new_data], ignore_index=True)
            else:
                updated_data = new_data
            
            updated_data.to_excel(file_path, index=False)
            st.success("✅ Your information has been successfully saved!")

    if st.button("View Submissions"):
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            st.dataframe(df)
        else:
            st.warning("No submissions found.")

if __name__ == "__main__":
    main()
