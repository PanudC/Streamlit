# import libraries
from PIL import Image
import streamlit as st
import requests
import base64
from io import BytesIO
import json
import numpy as np
import pandas as pd
import os
from datetime import datetime

# set title of app

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

# if check_password():
if True:


    st.title("Food Classification Application")
    st.write("")

# Save multiple uploaded files into new folder
    uploaded_files = st.file_uploader("Upload files generated from Stray Scanner", accept_multiple_files=True)
   
    def save_uploaded_files(filelist):
        
        parent_dir = "/Users/keane/Desktop/FinalProj/Dataset"
        # convert to datetime
        dt = datetime.now()

        # convert timestamp to string in dd-mm-yyyy HH:MM:SS
        str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")
        dataset_folder = "Dataset- " + str_dt

        newpath = os.path.join(parent_dir, dataset_folder) 
        os.mkdir(newpath)

        for uploadedfile in filelist:
            with open(os.path.join(newpath,uploadedfile.name),"wb") as f:
                f.write(uploadedfile.getbuffer())

        return st.success("Files Saved to New Dataset Folder!")
    
    num_of_files = len(uploaded_files)

    if num_of_files > 0 and num_of_files < 7:
        save_uploaded_files(uploaded_files)

# # Save single uploaded file into new folder
#     file_up = st.file_uploader("Upload a file")

#     def save_uploadedfile(uploadedfile):
        
#         parent_dir = "/Users/keane/Desktop/FinalProj/Dataset"
#         # convert to datetime
#         dt = datetime.now()

#         # convert timestamp to string in dd-mm-yyyy HH:MM:SS
#         str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")
#         dataset_folder = "Dataset- " + str_dt

#         newpath = os.path.join(parent_dir, dataset_folder) 
#         os.mkdir(newpath)

#         with open(os.path.join(newpath,uploadedfile.name),"wb") as f:
#             f.write(uploadedfile.getbuffer())
#         return st.success("Saved File:{} to Dataset Folder".format(uploadedfile.name))
        
#     if file_up is not None:
#         file_details = {"FileName":file_up.name,"FileType":file_up.type}
        
#         save_uploadedfile(file_up)

# Old Code
    # def im_2_b64(image):
    #     buff = BytesIO()
    #     image.save(buff, format="JPEG")
    #     img_str = base64.b64encode(buff.getvalue())
    #     return img_str.decode('UTF-8')

    # def predict(image):
    #     url = 'http://3.7.129.221:8000/foodapi/predict'

    #     obj = {'image': im_2_b64(image)}
    #     x = requests.post(url, json = obj)
        
    #     return x.text

    # if file_up is not None:
    #     # display image that user uploaded
    #     image = Image.open(file_up).convert('RGB')
    #     st.image(image, caption = 'Uploaded Image.', use_column_width = True)
    #     st.write("")
    #     st.write("Just a second ...")
    #     labels = predict(image)

    #     # print out the top 5 prediction labels with scores
    #     for food_item in json.loads(labels)["predict"]:
    #         st.write(food_item["name"])


        # st.json(labels)
    
    # def selectbox():
    #     df = pd.DataFrame({
    #         'first column': [1, 2, 3, 4],
    #         'second column': [10, 20, 30, 40]
    #      })

    #     option = st.selectbox(
    #         'Which number do you like best?',
    #         df['first column'])

    #     'You selected: ', option

    # selectbox()