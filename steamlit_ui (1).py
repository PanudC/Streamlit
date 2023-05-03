# import libraries
from PIL import Image
import streamlit as st
import requests
import base64
from io import BytesIO
import json

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


    st.title("Food Image Classification Application")
    st.write("")

    # enable users to upload images for the model to make predictions
    file_up = st.file_uploader("Upload an image", type = ["jpg","jpeg","png",'webp'])

    def im_2_b64(image):
        buff = BytesIO()
        image.save(buff, format="JPEG")
        img_str = base64.b64encode(buff.getvalue())
        return img_str.decode('UTF-8')

    def predict(image):
        url = 'http://localhost:8000/foodapi/predict'

        obj = {'image': im_2_b64(image)}
        x = requests.post(url, json = obj)
        
        return x.text

    if file_up is not None:
        # display image that user uploaded
        image = Image.open(file_up).convert('RGB')
        st.image(image, caption = 'Uploaded Image.', use_column_width = True)
        st.write("")
        st.write("Just a second ...")
        labels = predict(image)

        # print out the top 5 prediction labels with scores
        for food_item in json.loads(labels)["predict"]:
            st.write(food_item["name"])


        # st.json(labels)