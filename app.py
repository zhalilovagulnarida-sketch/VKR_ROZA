<<<<<<< HEAD
import streamlit as st

from PIL import Image

from model import predict

st.set_page_config(
    page_title="Lung Cancer AI",
    layout="centered"
)

st.title(
    "Lung Cancer Detection"
)

uploaded_file = st.file_uploader(
    "Upload image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("Analyzing image..."):

        diagnosis, confidence, probabilities = predict(image)

    st.success(
        f"Prediction: {diagnosis}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )

    st.subheader("Probabilities")

    for class_name, prob in probabilities.items():

        st.write(
            f"{class_name}: {prob:.2f}%"
=======
import streamlit as st

from PIL import Image

from model import predict

st.set_page_config(
    page_title="Lung Cancer AI",
    layout="centered"
)

st.title(
    "Lung Cancer Detection"
)

uploaded_file = st.file_uploader(
    "Upload image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner("Analyzing image..."):

        diagnosis, confidence, probabilities = predict(image)

    st.success(
        f"Prediction: {diagnosis}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )

    st.subheader("Probabilities")

    for class_name, prob in probabilities.items():

        st.write(
            f"{class_name}: {prob:.2f}%"
>>>>>>> c1394cf (Initial commit)
        )